import json
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "db" / "tododb.json"


def _to_dict(todo):
    # Use JSON mode so UUID values are converted to strings for file storage.
    return todo.model_dump(mode="json") if hasattr(todo, "model_dump") else dict(todo)


def _load_db():
    try:
        with open(DB_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        data = {}
    return {
        "todos": data.get("todos", []),
        "users": data.get("users", []),
    }


def _save_db(data):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def _save_todos(todos):
    db = _load_db()
    db["todos"] = todos
    _save_db(db)

def get_all_todos():
    return _load_db()["todos"]
    
def add_todo(todo):
    todos = get_all_todos()
    todo_data = _to_dict(todo)
    todos.append(todo_data)
    _save_todos(todos)
    return todo_data

def update_todo(todo_id, updated_todo):
    todos = get_all_todos()
    todo_id = str(todo_id)
    updated_todo_data = _to_dict(updated_todo)
    for i, todo in enumerate(todos):
        if str(todo["id"]) == todo_id:
            todos[i] = updated_todo_data
            _save_todos(todos)
            return updated_todo_data
    return None

def delete_todo(todo_id):
    todos = get_all_todos()
    todo_id = str(todo_id)
    for i, todo in enumerate(todos):
        if str(todo["id"]) == todo_id:
            deleted_todo = todos.pop(i)
            _save_todos(todos)
            return deleted_todo
    return None
