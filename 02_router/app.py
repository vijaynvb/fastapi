from fastapi import APIRouter, FastAPI
import uvicorn 

app = FastAPI(
    title="My API",
    description="This is a sample API",
    version="1.0.0"
)

global_router = APIRouter(prefix="/api/v1")
employee_router = APIRouter(prefix="/employees")
department_router = APIRouter(prefix="/departments")

# api/v1/employees 
# api/v1/departments

@employee_router.get("/")
def read_root():
    return {"name": "vijay", "age": 30}

global_router.include_router(employee_router)
app.include_router(global_router)
