from fastapi import FastAPI, WebSocket

app = FastAPI()


# Create a WebSocket endpoint
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    # Wait for messages from the client
    while True:
        message = await websocket.receive_text()
        print(f"Received message: {message}")
        response = f"Received message: {message}"
        await websocket.send_text(response)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8500)