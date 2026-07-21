
from fastapi import APIRouter
from services.todoFileDB import get_all_todos

global_router_v1 = APIRouter(prefix="/api/v1")
todo_router_v1 = APIRouter(prefix="/todos", tags=["Todos"])

@todo_router_v1.get("/",tags=["Todos"], summary="Get all todos", description="Get all todos from the database")
def read_root_v1():
    todos = get_all_todos()
    return todos

global_router_v1.include_router(todo_router_v1)