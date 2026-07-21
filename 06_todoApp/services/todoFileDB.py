import json
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "db" / "todo.json"

def get_all_todos():
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)