from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: str = None
    completed: bool = None

class TodoOut(TodoBase):
    id: int
    title: str
    completed: bool

    class Config:
        orm_mode = True