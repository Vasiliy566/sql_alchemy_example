import asyncio
import time


async def get_page():
    print("Starting to download page")
    await asyncio.sleep(3)
    print("Done downloading page")
    return "<html>Hello</html>"


async def read_db():
    print("Starting to retrieve data from db")
    await asyncio.sleep(3)
    print("Connected to db")
    await asyncio.sleep(1.5)
    print("Done retrieving data from db")
    return "db-data"


async def run():
    start = time.time()

    task1 = asyncio.create_task(get_page())
    task2 = asyncio.create_task(read_db())

    await task1
    await task2

    print(f"Time elapsed: {time.time() - start:.3}s")

asyncio.run(run())
