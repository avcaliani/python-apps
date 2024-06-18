from asyncio import sleep, run, ensure_future, gather
from random import choice
from time import time
from typing import Tuple, Any

from aiohttp import ClientSession

API_URL = "http://127.0.0.1:8000/item"
ERROR_THRESHOLD = 10

COLORS = [
    "31",  # Red
    "32",  # Green
    "33",  # Yellow
    "34",  # Blue
    "35",  # Magenta
    "36",  # Cyan
    "38;5;202",  # Orange
]


def color(value: Any) -> str:
    return f"\033[1;{choice(COLORS)}m{value}\033[00m"


async def get_item(session: ClientSession, item_id: int) -> Tuple[int, dict]:
    error, log_id = 0, color(item_id)
    while error < ERROR_THRESHOLD:
        async with session.get(f"{API_URL}/{item_id}") as resp:
            print(f"[{log_id}] status: {resp.status} | run: {error + 1}")
            if resp.status == 200:
                return resp.status, await resp.json()
            error += 1
            await sleep(5)
    return -1, {}


async def main():
    async with ClientSession() as session:
        tasks = [
            ensure_future(get_item(session, i)) for i in range(0, 6)
        ]
        data = await gather(*tasks)
        for item in data:
            print(f"[{item[0]}] {item[1]}")


if __name__ == "__main__":
    start_time = time()
    run(main())
    print(f"Elapsed time: {round(time() - start_time, 2)}")
