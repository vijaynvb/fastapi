from fastapi import APIRouter, FastAPI
from router.todoRouter import todo_router_v1
from router.userRouter import user_router_v1

# httpclient, ftpclient, smtpclient 

app = FastAPI(title="Todo App")
global_router_v1 = APIRouter(prefix="/api/v1")

global_router_v1.include_router(todo_router_v1)
global_router_v1.include_router(user_router_v1)
app.include_router(global_router_v1)