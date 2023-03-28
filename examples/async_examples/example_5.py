import heapq
import time
from collections import deque


def scheduler(coros):
    start = time.time()
    ready = deque(coros)
    sleeping = []
    while True:
        if not ready and not sleeping:
            break

        # wait for nearest sleeper,
        # if no coro can be executed immediately right now
        if not ready:
            deadline, coro = heapq.heappop(sleeping)
            if deadline > time.time():
                time.sleep(deadline - time.time())
            ready.append(coro)

        try:
            coro = ready.popleft()
            result = coro.send(None)
            # the special case of a coro that wants to be put to sleep
            if len(result) == 2 and result[0] == "sleep":
                deadline = time.time() + result[1]
                heapq.heappush(sleeping, (deadline, coro))
            else:
                print(f"Got: {result}")
                ready.append(coro)
        except StopIteration:
            pass
        print(f"Time elapsed: {time.time() - start:.3}s")


def get_page():
    print("Starting to download page")
    yield ("sleep", 1)
    print("Done downloading page")
    yield "<html>Hello</html>"


def read_db():
    print("Starting to retrieve data from db")
    yield ("sleep", 0.5)
    print("Connected to db")
    yield ("sleep", 1)
    print("Done retrieving data from db")
    yield "db-data"


scheduler([get_page(), read_db()])
