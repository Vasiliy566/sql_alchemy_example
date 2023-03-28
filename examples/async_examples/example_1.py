def coro():
    while True:
        print("Started")
        value = yield
        print(f"Got: {value}")


c = coro()
c.send(None)
c.send("Hello")
c.send("World")