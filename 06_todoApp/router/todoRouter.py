
from fastapi import APIRouter
from uuid import UUID, uuid4

from schema.todoSchema import ResponseTodo, Todo, TodoCreate, TodoUpdate
from services.todoFileDB import get_all_todos, add_todo, update_todo, delete_todo
from exceptions.TodoNotFoundException import TodoNotFoundException

todo_router_v1 = APIRouter(prefix="/todos", tags=["Todos"])

@todo_router_v1.get("/",tags=["Todos"], response_model=list[ResponseTodo], summary="Get all todos", description="Get all todos from the database")
def read_root_v1():
    todos = get_all_todos()
    return todos

@todo_router_v1.get("/{todo_id}",tags=["Todos"], response_model=ResponseTodo, summary="Get a todo by id", description="Get a todo by id from the database")
def read_todo_v1(todo_id: UUID):
    todo = next((todo for todo in get_all_todos() if str(todo["id"]) == str(todo_id)), None)
    if todo is None:
        raise TodoNotFoundException(todo_id=todo_id)
    return todo

# return the data to client after creating, updating, and deleting the data in the database 
@todo_router_v1.post("/",tags=["Todos"], response_model=ResponseTodo, summary="Create a new todo", description="Create a new todo in the database")
def create_todo_v1(todo: TodoCreate): # accepting the data from client and storing it in the database
    new_todo = Todo(id=uuid4(), title=todo.title, description=todo.description, completed=todo.completed)
    added_todo = add_todo(new_todo)
    return added_todo

@todo_router_v1.put("/{todo_id}",tags=["Todos"],response_model=ResponseTodo, summary="Update a todo by id", description="Update a todo by id in the database")
def update_todo_v1(todo_id: UUID, updated_todo: TodoUpdate): # accepting the data from client and updating it in the database
    updated_todo_data = Todo(id=todo_id, title=updated_todo.title, description=updated_todo.description, completed=updated_todo.completed)
    updated_todo = update_todo(todo_id, updated_todo_data)
    if updated_todo is None:
        raise TodoNotFoundException(todo_id=todo_id)
    return updated_todo

@todo_router_v1.delete("/{todo_id}",tags=["Todos"], response_model=ResponseTodo, summary="Delete a todo by id", description="Delete a todo by id from the database")
def delete_todo_v1(todo_id: UUID):
    deleted_todo = delete_todo(todo_id)
    if deleted_todo is None:
        raise TodoNotFoundException(todo_id=todo_id) # object is created todonotfoundexception and passed the todo_id to the constructor of the class and then raised the exception
    return deleted_todo
