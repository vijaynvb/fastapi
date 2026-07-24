from fastapi import APIRouter, FastAPI
import uvicorn 

app = FastAPI(
    title="My API",
    description="This is a sample API",
    version="1.0.0"
)

global_router_v1 = APIRouter(prefix="/api/v1")
global_router_v2 = APIRouter(prefix="/api/v2")
employee_router_v1 = APIRouter(prefix="/employees")
employee_router_v2 = APIRouter(prefix="/employees")

# api/v1/employees

@employee_router_v1.get("/")
def read_root_v1():
    return {"name": "vijay", "age": 30}

@employee_router_v2.get("/")
def read_root_v2():
    return {"name": "vijay", "age": 30}

global_router_v1.include_router(employee_router_v1)
global_router_v2.include_router(employee_router_v2)
app.include_router(global_router_v1)
app.include_router(global_router_v2)