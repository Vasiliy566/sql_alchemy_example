import uvicorn
from fastapi import FastAPI

from app.routes.items import router

app = FastAPI()
app.include_router(router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
