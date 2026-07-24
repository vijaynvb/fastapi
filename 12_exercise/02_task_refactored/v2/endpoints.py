

from fastapi import APIRouter


global_router_v2 = APIRouter(prefix="/api/v2")
employee_router_v2 = APIRouter(prefix="/employees")
@employee_router_v2.get("/")
def read_root_v2():
    return {"name": "vijay", "age": 30}

global_router_v2.include_router(employee_router_v2)