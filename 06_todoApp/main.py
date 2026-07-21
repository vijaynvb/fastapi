from fastapi import FastAPI
from router.todoRouter import global_router_v1
app = FastAPI(title="Todo App")
app.include_router(global_router_v1)