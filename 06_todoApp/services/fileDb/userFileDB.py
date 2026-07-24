import json
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "db" / "tododb.json"

def _to_dict(user):
    # Use JSON mode so UUID values are converted to strings for file storage.
    return user.model_dump(mode="json") if hasattr(user, "model_dump") else dict(user)


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


def _save_users(users):
    db = _load_db()
    db["users"] = users
    _save_db(db)


def get_all_users():
    return _load_db()["users"]
    
def add_user(user):
    users = get_all_users()
    user_data = _to_dict(user)
    users.append(user_data)
    _save_users(users)
    return user_data

def update_user(user_id, updated_user):
    users = get_all_users()
    user_id = str(user_id)
    updated_user_data = _to_dict(updated_user)
    for i, user in enumerate(users):
        if str(user["id"]) == user_id:
            users[i] = updated_user_data
            _save_users(users)
            return updated_user_data
    return None

def delete_user(user_id):
    users = get_all_users()
    user_id = str(user_id)
    for i, user in enumerate(users):
        if str(user["id"]) == user_id:
            deleted_user = users.pop(i)
            _save_users(users)
            return deleted_user
    return None
