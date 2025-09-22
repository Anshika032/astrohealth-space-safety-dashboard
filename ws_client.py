import asyncio, websockets 
 
async def listen(): 
    url = "ws://127.0.0.1:8000/ws/telemetry" 
    async with websockets.connect(url) as ws: 
        print(f"Connected to {url}") 
        while True: 
            try: 
                msg = await ws.recv() 
                print("[WS MESSAGE]", msg) 
            except Exception as e: 
                print("Connection closed:", e) 
                break 
 
if __name__ == "__main__": 
    asyncio.run(listen())
