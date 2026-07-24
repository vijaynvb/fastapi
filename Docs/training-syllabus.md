# FastAPI Training Syllabus

## 1. Core Concepts Before FastAPI

### Microservices Principles
- Small, focused services
- Independent deployment and scaling
- Clear service boundaries
- API-based communication
- Resilience and observability

### HTTP
- Request/response model
- Methods: GET, POST, PUT, DELETE
- URLs, headers, body, status codes
- Client/server communication

### JSON
- Common API payload format
- Objects and arrays
- Serialization and deserialization
- Input/output validation

### REST
- Resource-oriented design
- Stateless APIs
- CRUD mapped to HTTP verbs
- Consistent status codes and versioning

## 2. FastAPI Topics in This Repo

### 01_basic
- App creation and metadata
- Path parameters and query parameters
- Type validation
- Uvicorn startup

### 02_router
- APIRouter usage
- Route grouping and nesting
- Prefix-based versioning

### 03_schemas
- Request and response schemas
- Pydantic models
- response_model usage

### 04_models
- Placeholder for model-focused examples
- Useful for ORM/domain modeling lessons

### 05_envVariables
- Environment-based configuration
- BaseSettings and .env usage
- Separation of config from code

### 06_todoApp
- Modular FastAPI application structure
- JSON file persistence
- Middleware, exceptions, and logging
- Health and metrics endpoints
- JSON/XML content negotiation

### 07_middleware
- Middleware flow
- Request/response interception
- Security, logging, and response handling examples

### 08_rdbms
- FastAPI with PostgreSQL and SQLAlchemy
- Dependency injection with DB sessions
- CRUD, pagination, and error handling

### 09_DI
- Dependency injection concepts
- Loose coupling with interfaces
- Dynamic class/module loading
- Strategy-style algorithm switching

### 10_exercise
- Versioned APIs and refactoring practice
- OpenAPI customization
- Capstone-style API design exercises
- AWS AI services API layer exercise

## 3. Recommended Teaching Order
1. HTTP, JSON, REST, and microservices basics
2. FastAPI basics with routing
3. Schemas and validation
4. Configuration and middleware
5. Modular CRUD application design
6. Database-backed APIs
7. Dependency injection patterns
8. Capstone exercises and refactoring
