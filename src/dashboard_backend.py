import asyncio, threading, json, os, time, random
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
    for ws in connections:
        try:
            await ws.send_json(message)
        except:
            dead.append(ws)
    for ws in dead:
        connections.remove(ws)

# WebSocket endpoint
@app.websocket("/ws/telemetry")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    connections.add(ws)
    try:
        while True:
            await asyncio.sleep(1)  # keep alive
    except:
        connections.remove(ws)

# Background: Fake alerts every 5 seconds
async def generate_fake_alerts():
    while True:
        alert = {
            "alert": "Demo Conjunction",
            "object": "SAT-1 vs DEBRIS-1",
            "min_distance_km": round(5 + random.random() * 5, 2),
            "time": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        await broadcast({"topic": "space/alerts/collision", "payload": alert})
        await asyncio.sleep(5)

# Background: Fake summary every 60 seconds
async def generate_fake_summary():
    while True:
        summary = {
            "active_sats": random.randint(3000, 4000),
            "debris": random.randint(25000, 28000),
            "close_approaches": random.randint(10, 25)
        }
        await broadcast({"topic": "space/summary", "payload": summary})
        await asyncio.sleep(60)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(generate_fake_alerts())
    asyncio.create_task(generate_fake_summary())

if __name__ == "__main__":
    uvicorn.run("src.dashboard_backend:app", host="0.0.0.0", port=8000, reload=True)
