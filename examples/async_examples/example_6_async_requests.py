import asyncio
import time
from aiohttp import ClientSession


async def get_my_temp(lat: float, lon: float) -> float:
    async with ClientSession() as session:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        async with session.get(url=url) as resp:
            res = await resp.json()
            return res["current_weather"]["temperature"]


async def run(data):
    tasks = []
    for lan, lot in data:
        task = asyncio.create_task(get_my_temp(lan, lot))
        tasks.append(task)

    res = await asyncio.gather(*tasks)
    for r in res:
        print(r)


data = [(0, 0), (1, 15), (2, 10), (3, 11), (50, 60), (40, 50)] * 3000

start = time.time()

asyncio.run(run(data))

print(f"{time.time() - start}s")
