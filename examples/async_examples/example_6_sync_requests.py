import time

import requests


def get_my_temp(lat: float, lon: float) -> float:
    r = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true")

    return r.json()["current_weather"]["temperature"]


data = [(0, 0), (1, 15), (2, 10), (3, 11), (50, 60), (40, 50)] * 3

start = time.time()

for lan, lot in data:
    print(get_my_temp(lan, lot))

print(f"{time.time() - start}s")
