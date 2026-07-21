
import json

from fastapi import APIRouter
from services.todoFileDB import get_all_todos, add_todo, update_todo, delete_todo

global_router_v1 = APIRouter(prefix="/api/v1")
todo_router_v1 = APIRouter(prefix="/todos", tags=["Todos"])

@todo_router_v1.get("/",tags=["Todos"], summary="Get all todos", description="Get all todos from the database")
def read_root_v1():
    todos = get_all_todos()
    return todos

@todo_router_v1.get("/{todo_id}",tags=["Todos"], summary="Get a todo by id", description="Get a todo by id from the database")
def read_todo_v1(todo_id: int):
    todo = next((todo for todo in get_all_todos() if todo["id"] == todo_id), None)
    if todo is None:
        return {"error": "Todo not found"}
    return todo

@todo_router_v1.post("/",tags=["Todos"], summary="Create a new todo", description="Create a new todo in the database")
def create_todo_v1(todo: dict):
    add_todo(todo)
    return todo

@todo_router_v1.put("/{todo_id}",tags=["Todos"], summary="Update a todo by id", description="Update a todo by id in the database")
def update_todo_v1(todo_id: int, updated_todo: dict):
    updated_todo = update_todo(todo_id, updated_todo)
    if updated_todo is None:
        return {"error": "Todo not found"}
    return updated_todo

@todo_router_v1.delete("/{todo_id}",tags=["Todos"], summary="Delete a todo by id", description="Delete a todo by id from the database")
def delete_todo_v1(todo_id: int):
    deleted_todo = delete_todo(todo_id)
    if deleted_todo is None:
        return {"error": "Todo not found"}
    return deleted_todo

global_router_v1.include_router(todo_router_v1)