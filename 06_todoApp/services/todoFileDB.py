import json
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "db" / "todo.json"

def get_all_todos():
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
    
def add_todo(todo):
    todos = get_all_todos()
    todos.append(todo)
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=4)

def update_todo(todo_id, updated_todo):
    todos = get_all_todos()
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todos[i] = updated_todo
            with open(DB_PATH, "w", encoding="utf-8") as f:
                json.dump(todos, f, ensure_ascii=False, indent=4)
            return updated_todo
    return None
def delete_todo(todo_id):
    todos = get_all_todos()
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            deleted_todo = todos.pop(i)
            with open(DB_PATH, "w", encoding="utf-8") as f:
                json.dump(todos, f, ensure_ascii=False, indent=4)
            return deleted_todo
    return None
