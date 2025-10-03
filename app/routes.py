from fastapi import APIRouter
from .db import db


router = APIRouter()


@router.get("/users")
def get_users():
    users = list(db.users.find({}, {"_id": 0}))
    return {"users": users}
