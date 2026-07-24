import json
from pathlib import Path
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from models.userModel import User
from schemas.userSchema import UserOut
from dotenv import load_dotenv
import os

USER_DB_PATH = Path(__file__).parent.parent / "db" / "user.json"

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def read_users():
    if not USER_DB_PATH.exists() or USER_DB_PATH.stat().st_size == 0:
        # Initialize admin user if file is empty
        admin_user = [{
            "id": 1,
            "username": "admin",
            "hashed_password": pwd_context.hash("admin"),
            "role": "admin"
        }]
        with open(USER_DB_PATH, "w", encoding="utf-8") as f:
            json.dump(admin_user, f, indent=2)
        return admin_user
    with open(USER_DB_PATH, "r", encoding="utf-8") as f:
        users_raw = json.load(f)
    return [User(**user) for user in users_raw]

def write_users(users):
    users_dict = [user.__dict__ if isinstance(user, User) else user for user in users]
    with open(USER_DB_PATH, "w", encoding="utf-8") as f:
        json.dump(users_dict, f, indent=2)

def get_user(username: str):
    users = read_users()
    for user in users:
        if user.username == username:
            return user
    return None

def get_user_by_id(user_id: int):
    users = read_users()
    for user in users:
        if user.id == user_id:
            return user
    return None

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not pwd_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(username)
    if user is None:
        raise credentials_exception
    return user

def get_current_admin(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required"
        )
    return current_user

def signup_user(username: str, password: str):
    users = read_users()
    if get_user(username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )
    new_id = max([user.id for user in users], default=0) + 1
    user = User(
        id=new_id,
        username=username,
        hashed_password=pwd_context.hash(password),
        role="user"
    )
    users.append(user)
    write_users(users)
    return user
