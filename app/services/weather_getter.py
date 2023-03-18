import requests

lat = 59.938480
lon = 30.312481


def get_my_temp(lat: float, lon: float) -> float:
    r = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true")

    return r.json()["current_weather"]["temperature"]


def get_close(lat: float, lon: float) -> str:
    temp = get_my_temp(lat, lon)
    if temp > 20:
        return "На улице жарко, надеть футболку"
    else:
        return "На улице холодно, надеть шубу"


if __name__ == "__main__":
    r = get_my_temp(lat, lon)
    print(r)
