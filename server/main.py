import asyncio
import json
from contextlib import asynccontextmanager

import websockets
from api.v1.api import api_router
from core.configs import settings
from fastapi import FastAPI

WEBSOCKET_PORT = 8001
connections = {}


async def websocket_server(websocket, _):
    user_uid = None
    try:
        async for client in websocket:
            client = json.loads(client)
            action = client.get("action")
            data = client.get("data")

            # Handle login action
            if action == "login" and "user_uid" in client:
                user_uid = client["user_uid"]
                
                if user_uid not in connections:
                    connections[user_uid] = websocket
                    print(f"{client['username']} connected to the server!")
                    await websocket.send(f"{client['username']} connected to the server!")

            # Handle users action
            elif action == "users":
                print("WEBSOCKET: USERS")

            # Handle contacts action
            elif action == "contacts":
                user_uid = data[0].get("user_uid", None)
                
                for user, conn in connections.items():
                    if user == user_uid:
                        await conn.send(json.dumps(data[0]))

            # Handle message action
            elif action == "message" and "content" in data:
                sender = data.get("sender", None)
                recipient = data.get("recipient", None)

                if sender is None or recipient is None:
                    return

                message = data["content"]
                for user, conn in connections.items():
                    if user == recipient:
                        print(f"{sender} to {recipient}")  # TODO Add log
                        response_data = {"sender": sender, "message": message}
                        await conn.send(json.dumps(response_data))

    except websockets.exceptions.ConnectionClosed:
        print("A client just disconnected")
    finally:
        if user_uid and user_uid in connections:
            del connections[user_uid]


async def start_websocket_server():
    print("WebSocket server listening on", WEBSOCKET_PORT)
    server = await websockets.serve(websocket_server, "localhost", WEBSOCKET_PORT)
    await server.wait_closed()


@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(start_websocket_server())
    yield


app = FastAPI(title="iText", version="1.0.0", lifespan=lifespan)
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
