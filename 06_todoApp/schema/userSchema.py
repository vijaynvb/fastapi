from pydantic import BaseModel
from uuid import UUID


class User(BaseModel):
    id: UUID
    username: str
    email: str

class UserCreate(BaseModel):
    username: str
    email: str

class UserUpdate(BaseModel):
    username: str | None = None
    email: str | None = None

class ResponseUser(BaseModel):
    id: UUID
    username: str
    email: str