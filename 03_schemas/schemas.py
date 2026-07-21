from pydantic import BaseModel
import uuid

class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool

class ResponseEmployeeSchema(BaseModel):
    id: uuid.UUID
    name: str
    position: str
    salary: float
    is_active: bool

class RequestEmployeeSchema(BaseModel):
    name: str
    position: str
    salary: float
    is_active: bool


class DepartmentSchema(BaseModel):
    id: int
    name: str
    manager_id: int
    is_active: bool