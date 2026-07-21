from pydantic import BaseModel
class Todo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

class TodoCreate(BaseModel):
    title: str
    description: str
    completed: bool = False

class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None

class ResponseTodo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool