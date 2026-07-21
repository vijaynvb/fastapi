
from fastapi import APIRouter
from uuid import UUID, uuid4

from schema.userSchema import ResponseUser, User, UserCreate, UserUpdate
from services.userFileDB import get_all_users, add_user, update_user, delete_user

user_router_v1 = APIRouter(prefix="/users", tags=["Users"])

@user_router_v1.get("/",tags=["Users"], summary="Get all users", description="Get all users from the database")
def read_root_v1():
    users = get_all_users()
    return users

@user_router_v1.get("/{user_id}",tags=["Users"], summary="Get a user by id", description="Get a user by id from the database")
def read_user_v1(user_id: UUID):
    user = next((user for user in get_all_users() if str(user["id"]) == str(user_id)), None)
    if user is None:
        return {"error": "User not found"}
    return user

@user_router_v1.post("/",tags=["Users"], response_model=ResponseUser, summary="Create a new user", description="Create a new user in the database")
def create_user_v1(user: UserCreate):
    new_user = User(id=uuid4(), username=user.username, email=user.email)
    added_user = add_user(new_user)
    return added_user

@user_router_v1.put("/{user_id}",tags=["Users"], response_model=ResponseUser, summary="Update a user by id", description="Update a user by id in the database")
def update_user_v1(user_id: UUID, updated_user: UserUpdate):
    updated_user_data = User(id=user_id, username=updated_user.username, email=updated_user.email)
    updated_user = update_user(user_id, updated_user_data)
    if updated_user is None:
        return {"error": "User not found"}
    return updated_user

@user_router_v1.delete("/{user_id}",tags=["Users"], summary="Delete a user by id", description="Delete a user by id from the database")
def delete_user_v1(user_id: UUID):
    deleted_user = delete_user(user_id)
    if deleted_user is None:
        return {"error": "User not found"}
    return deleted_user
