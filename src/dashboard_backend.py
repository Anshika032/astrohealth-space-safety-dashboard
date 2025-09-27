import asyncio, json, os, time, random
from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()
connections = set()

# Serve static files (frontend)
frontend_path = os.path.join(os.path.dirname(__file__), "frontend")
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

@app.get("/")
async def serve_index():
    return FileResponse(os.path.join(frontend_path, "index.html"))

# Broadcast helper
async def broadcast(message):
    dead = []
    for ws in list(connections):
        try:
            await ws.send_json(message)
        except Exception:
            dead.append(ws)
    for ws in dead:
        connections.discard(ws)   # ✅ safe removal

# WebSocket endpoint
@app.websocket("/ws/telemetry")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    connections.add(ws)
    try:
        while True:
            await asyncio.sleep(1)  # keep alive
    except Exception:
        connections.discard(ws)   # ✅ safe removal

# ----------------------------
# Background: Fake alerts every 5 seconds
# ----------------------------
async def generate_fake_alerts():
    while True:
        # randomize distance and objects a bit
        obj_a = f"SAT-{random.randint(1,9)}"
        obj_b = f"DEBRIS-{random.randint(1,99)}"
        md = round(3 + random.random() * 15, 2)  # 3–18 km
        alert = {
            "alert": "Demo Conjunction",
            "object": f"{obj_a} vs {obj_b}",
            "min_distance_km": md,
            "time": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        }
        print("Sent alert:", alert)
        await broadcast({"topic": "space/alerts/collision", "payload": alert})
        await asyncio.sleep(5)

# ----------------------------
# Background: Fake summary every 60 seconds
# ----------------------------
async def generate_fake_summary():
    while True:
        summary = {
            "active_sats": random.randint(3000, 4000),
            "debris": random.randint(25000, 28000),
            "close_approaches": random.randint(10, 25)
        }
        print("Sent summary:", summary)
        await broadcast({"topic": "space/summary", "payload": summary})
        await asyncio.sleep(60)

# ----------------------------
# Background: Fake astronaut health every 5 seconds
# ----------------------------
def rand_bone():
    # Typical astronaut concerns: T-score shift negative; BMD 0.8–1.3
    bmd = round(random.uniform(0.80, 1.30), 2)
    # T-score rough sim: -3.0 (low) to +1.0 (high-normal)
    tscore = round(random.uniform(-3.0, 1.0), 2)
    return bmd, tscore

async def generate_fake_health():
    while True:
        bmd, tscore = rand_bone()
        health = {
            "channel": "health",
            "data": {
                # Pulse/HR
                "hr": random.randint(55, 130),     # bpm
                "spo2": random.randint(85, 100),   # %
                "stress": random.randint(1, 5),    # 1–5
                # New vitals
                "resp": random.randint(8, 28),             # rpm
                "temp": round(random.uniform(35.5, 38.8), 1),  # °C
                "bp_sys": random.randint(90, 150),  # mmHg
                "bp_dia": random.randint(55, 100),  # mmHg
                "bone_bmd": bmd,                    # g/cm^2
                "bone_tscore": tscore               # T-score
            }
        }
        print("Sent health:", health)
        await broadcast(health)
        await asyncio.sleep(5)

# ----------------------------
# Startup: launch all background tasks
# ----------------------------
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(generate_fake_alerts())
    asyncio.create_task(generate_fake_summary())
    asyncio.create_task(generate_fake_health())

# ----------------------------
# Main entry
# ----------------------------
if __name__ == "__main__":
    # Adjust module path below to your actual module if needed
    uvicorn.run("src.dashboard_backend:app", host="0.0.0.0", port=8000, reload=True)
