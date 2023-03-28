import time
from datetime import datetime

from fastapi import APIRouter, HTTPException, Depends, Header
from pydantic import BaseModel

from app.db.db_user import db_users_fabric
from app.services.weather_getter import get_close

router = APIRouter(
    prefix="/api",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


class UserResponse(BaseModel):
    id: int
    name: str
    birthday: datetime
    work_quality: int
    password: str
    comment: str | None
    comment2: str | None

    class Config:
        orm_mode = True


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(
        user_id: int,
        x_api_key: str | None = Header(default=None)
) -> UserResponse:
    if x_api_key != "123321":
        raise HTTPException(status_code=401, detail=f"Wrong api key")
    user = db_users_fabric().get({"id": user_id})
    if user is None:
        raise HTTPException(status_code=404, detail=f"User not found")
    return user


@router.get("/get_close")
def get_close_(
        lat: float,
        lon: float
):
    time.sleep(20)
    return get_close(lat, lon)
