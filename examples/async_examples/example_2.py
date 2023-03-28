def coro1():
    print("coro1 doing some work")
    yield
    print("coro1 doing some work")
    yield


def coro2():
    print("coro2 doing some work")
    yield
    print("coro2 doing some work")
    yield


def scheduler():
    c1 = coro1()
    c2 = coro2()
    c1.send(None)
    c2.send(None)
    c1.send(None)
    c2.send(None)


scheduler()
