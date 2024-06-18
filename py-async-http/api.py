from random import choice

from fastapi import FastAPI, HTTPException

MOCK_DB = {
    "1": {"emoji": "🏈", "queries": 0},
    "2": {"emoji": "🗿", "queries": 0},
    "3": {"emoji": "🐍", "queries": 0},
    "4": {"emoji": "💎", "queries": 0},
    "5": {"emoji": "🍩️", "queries": 0},
}
app = FastAPI()


@app.get("/item/{item_id}")
async def item(item_id: str) -> dict:

    if choice([True, False]):
        raise HTTPException(status_code=500, detail=f"Server instability 🤒")

    data = MOCK_DB.get(item_id)
    if not data:
        raise HTTPException(status_code=404, detail=f"Item '{item_id}' not found 🤔")

    data["queries"] += 1
    return {
        "id": item_id,
        "emoji": data.get("emoji"),
        "queries": data.get("queries")
    }
