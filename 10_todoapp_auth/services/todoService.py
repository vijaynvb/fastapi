import json
from pathlib import Path
from models.todoModel import Todo

DB_PATH = Path(__file__).parent.parent / "db" / "todo.json"

def read_todos():
    if not DB_PATH.exists():
        return []
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def write_todos(todos):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(todos, f, indent=2)

def get_all_todos():
    return read_todos()

def get_todo(id: int):
    todos = read_todos()
    for todo in todos:
        if todo["id"] == id:
            return todo
    return None

def create_todo(data):
    todos = read_todos()
    new_id = max([todo["id"] for todo in todos], default=0) + 1
    todo = {"id": new_id, "title": data.title, "completed": False}
    todos.append(todo)
    write_todos(todos)
    return todo

def update_todo(id: int, data):
    todos = read_todos()
    for todo in todos:
        if todo["id"] == id:
            if data.title is not None:
                todo["title"] = data.title
            if data.completed is not None:
                todo["completed"] = data.completed
            write_todos(todos)
            return todo
    return None

def delete_todo(id: int):
    todos = read_todos()
    new_todos = [todo for todo in todos if todo["id"] != id]
    write_todos(new_todos)
    return None