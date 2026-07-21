from fastapi import FastAPI
from schemas import ResponseEmployeeSchema, RequestEmployeeSchema
import uvicorn
import uuid

employees: list[ResponseEmployeeSchema] = [
    ResponseEmployeeSchema(id=uuid.uuid4(), name="John Doe", position="Software Engineer", salary=80000.0, is_active=True),
    ResponseEmployeeSchema(id=uuid.uuid4(), name="Jane Smith", position="Data Scientist", salary=90000.0, is_active=True),
    ResponseEmployeeSchema(id=uuid.uuid4(), name="Mike Johnson", position="Product Manager", salary=95000.0, is_active=False),
    ResponseEmployeeSchema(id=uuid.uuid4(), name="Emily Davis", position="UX Designer", salary=70000.0, is_active=True),
]

app = FastAPI()

@app.get("/employees", response_model=list[ResponseEmployeeSchema], status_code=200)
def read_root():
    return employees

@app.post("/employees", response_model=ResponseEmployeeSchema, status_code=201)
def create_employee(employee: RequestEmployeeSchema):
    #uuid - unique identifier
    new_employee = ResponseEmployeeSchema(id=uuid.uuid4(), name=employee.name, position=employee.position, salary=employee.salary, is_active=employee.is_active)
    employees.append(new_employee)
    return new_employee