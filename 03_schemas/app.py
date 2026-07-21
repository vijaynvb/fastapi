from fastapi import FastAPI
from schemas import EmployeeSchema
import uvicorn 

employees: list[EmployeeSchema] = [
    EmployeeSchema(id=1, name="John Doe", position="Software Engineer", salary=80000.0, is_active=True),
    EmployeeSchema(id=2, name="Jane Smith", position="Data Scientist", salary=90000.0, is_active=True),
    EmployeeSchema(id=3, name="Mike Johnson", position="Product Manager", salary=95000.0, is_active=False),
    EmployeeSchema(id=4, name="Emily Davis", position="UX Designer", salary=70000.0, is_active=True),
]

app = FastAPI()

@app.get("/employees", response_model=list[EmployeeSchema])
def read_root():
    return employees

@app.post("/employees", response_model=EmployeeSchema, status_code=201)
def create_employee(employee: EmployeeSchema):
    employees.append(employee)
    return employee