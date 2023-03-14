from datetime import datetime

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel

from app.dependencies import get_user_dependency
from app.services.get_user_service import GetUser

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


@router.get("/users/{user_id}", response_model=UserResponse | None)
def get_user(
    user_id: int,
    get_user_service: GetUser = Depends(get_user_dependency)
) -> UserResponse | None:
    return get_user_service(user_id)

# @router.post("/items/{item_id}")
# def read_item2(item_id: int, q: int, item: Item):
#     return {"item_id": item_id, "name": item.name, "price": item.price, "is_offer": item.is_offer, "q": q}
