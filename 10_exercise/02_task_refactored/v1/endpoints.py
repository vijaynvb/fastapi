

from fastapi import APIRouter


global_router_v1 = APIRouter(prefix="/api/v1")
employee_router_v1 = APIRouter(prefix="/employees")
@employee_router_v1.get("/")
def read_root_v1():
    return {"name": "vijay", "age": 30}

global_router_v1.include_router(employee_router_v1)