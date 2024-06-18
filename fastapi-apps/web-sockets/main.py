from asyncio import sleep
from datetime import datetime
from random import choice
from time import sleep
from uuid import uuid4

from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get('/', response_class=HTMLResponse)
async def root():
    with open('static/index.html', 'r', encoding='utf8') as file:
        return HTMLResponse(content=file.read().rstrip(), status_code=200)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        received_at = datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S')
        if str(data) == 'close':
            return await websocket.close()
        await websocket.send_text(f'Message 👉 "{data}" 👈 was received at "{received_at}"')


@app.websocket("/ws/updates")
async def websocket_updates(websocket: WebSocket):
    await websocket.accept()
    conn_id, msg_n = str(uuid4()), 0
    while True:
        msg_n += 1
        data = await get_update(conn_id, msg_n)
        await websocket.send_json(data)


async def get_update(conn_id: str, count: int) -> dict:
    await sleep(choice([1, 3, 5]))
    return {
        'socket_id': conn_id,
        'count': count,
        'field': 'main_sport',
        'value': choice(['🏀', '🏈', '⚾️', '🎾', '🏐', '🎱'])
    }
