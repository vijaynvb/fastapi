from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    description: str
    completed: bool = False


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: str = None
    description: str = None
    completed: bool = None


class Todo(TodoBase):
    id: int

    class Config:
        from_attributes = True
