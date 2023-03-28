import uvicorn
from fastapi import FastAPI

from app.routes.items import router
from app.utils import fib

app = FastAPI()
app.include_router(router)


@app.get("/sum")
async def read_root(a: int, b: int):
    return a + b


@app.get("/fib")
async def fibonacci(n: int):
    return fib(n)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
