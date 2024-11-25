from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from utils.dataset_utils import index
from utils.chat_history import chat_memory, chat_store, chat_store_path
import os

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("WebSocket connection established.")
    
    try:
        while True:
            data = await websocket.receive_text() 
            print(f"User: {data}")
            await websocket.send_text(f"User: {data}")

            chat_engine = index.as_chat_engine(memory = chat_memory)
            response = str(chat_engine.chat(data))
            chat_store.persist(persist_path=chat_store_path)
            print(f"User: {response}")
            await websocket.send_text(f"Reply: {response}")
            
    except WebSocketDisconnect as e:
        print(f"WebSocket disconnected: {e}")




@router.get("/")
async def get():
    return FileResponse(os.path.join("view", "chat.html"))
