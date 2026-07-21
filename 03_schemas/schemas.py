from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool

class EmployeeSchema(BaseModel):
    id: int
    name: str
    position: str
    salary: float
    is_active: bool

class DepartmentSchema(BaseModel):
    id: int
    name: str
    manager_id: int
    is_active: bool