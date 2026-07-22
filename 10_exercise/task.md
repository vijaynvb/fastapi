
# Tasks

### Task 1
- Create a new FastAPI application with the following specifications:
  - Title: "My API"
  - Description: "This is a sample API"
  - Version: "1.0.0"

create endpoints for the following routes using APIRouter:
  - GET /api/v1/employees
  - GET /api/v2/employees


### Task 2

Task: Employee Management System (Feature-Parity Exercise)
Use this as your new assignment prompt.

Build a new FastAPI application called Employee Management System with API versioning at path prefix /api/v1.
Implement two resources:
Employee
Department
Replicate all major behaviors from the attached Todo app, including:
Router-based modular structure
File-based JSON persistence
Request logging middleware
Content negotiation middleware for JSON to XML
Health and metrics endpoints
Custom exception handling and global exception handling
Pydantic schemas for create, update, and response models
Functional Requirements
Employee Resource
Create endpoints:
GET /api/v1/employees/
GET /api/v1/employees/{employee_id}
POST /api/v1/employees/
PUT /api/v1/employees/{employee_id}
DELETE /api/v1/employees/{employee_id}
Use UUID for employee_id.
Use request/response schemas:
Employee
EmployeeCreate
EmployeeUpdate
ResponseEmployee
Department Resource
Create endpoints:
GET /api/v1/departments/
GET /api/v1/departments/{department_id}
POST /api/v1/departments/
PUT /api/v1/departments/{department_id}
DELETE /api/v1/departments/{department_id}
Use UUID for department_id.
Use request/response schemas:
Department
DepartmentCreate
DepartmentUpdate
ResponseDepartment
Persistence
Store data in a local JSON file under a db folder.
Keep both employees and departments in the same JSON file with top-level arrays:
employees
departments
Implement service-layer functions for each resource:
get_all
add
update
delete
Handle missing/invalid DB file safely.
Middleware
Add logging middleware that:
Generates or reads X-Request-ID
Logs method, path, client IP, status code, duration
Adds response headers:
X-Request-ID
X-Process-Time-ms
Add content negotiation middleware:
If Accept header contains application/xml, convert JSON response body to XML.
Skip docs/openapi/redoc routes from conversion.
Exception Handling
Add custom not-found exception for Employee and Department.
Register custom exception handlers.
Add global exception handler for unhandled exceptions returning JSON error payload.
Health and Metrics
Add:
GET /health
GET /api/v1/metrics/cpu
GET /api/v1/metrics/mem
Non-Functional Requirements
Keep a modular folder structure similar to the attached app:
config
db
exceptions
middlewares
router
schema
services
utils
Add API metadata (title at minimum).
Use clean, readable naming consistent across files.
Acceptance Criteria
All Employee and Department CRUD endpoints work end-to-end.
Data persists to JSON file between requests.
XML response is returned when Accept: application/xml is sent.
Request logs are written and include timing and request IDs.
Not-found paths return custom exception responses.
Health and metrics endpoints return valid JSON payloads.
Project structure is modular and consistent with source app patterns.