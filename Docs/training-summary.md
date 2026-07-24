# FastAPI Training Summary

## Part 1: Foundational Topics Covered Before FastAPI

### 1. Microservices Principles
- Single responsibility per service.
- Independent deployability and versioning.
- API-first communication between services.
- Decentralized data ownership per service boundary.
- Failure isolation and resilience (graceful error handling, health checks).
- Observability basics (logs, metrics, request IDs).

### 2. HTTP Fundamentals
- HTTP as a request-response protocol.
- Request structure: method, URI/path, version, headers, body.
- Response structure: status code, version, headers, body.
- Common methods used for APIs: GET, POST, PUT, DELETE.
- Status-code usage for API behavior (200, 201, 204, 404, 500).

### 3. JSON Fundamentals
- JSON as the primary API payload format.
- Object and array modeling for resources.
- Serialization/deserialization between Python models and JSON.
- Validation of JSON input using schemas.

### 4. REST Principles
- Resource-oriented URLs.
- Stateless request handling.
- CRUD mapping to HTTP verbs.
- Consistent response contracts and status codes.
- Versioned API patterns for backward compatibility.

These themes are explicitly echoed in the top-level repo recap in [readme.md](../readme.md).

## Part 2: Topics Covered in This Repository (Training Examples)

### 01_basic
File: [01_basic/app.py](../01_basic/app.py)
- FastAPI app bootstrap and metadata.
- Path parameters and query parameters.
- Type-based validation by FastAPI/Pydantic.
- Running app with Uvicorn.

### 02_router
File: [02_router/app.py](../02_router/app.py)
- Router composition with APIRouter.
- Prefix-based route grouping.
- Nested router inclusion.
- API version prefixing approach.

### 03_schemas
Files: [03_schemas/app.py](../03_schemas/app.py), [03_schemas/schemas.py](../03_schemas/schemas.py)
- Request and response schema separation.
- Pydantic models and typed contracts.
- response_model for output shaping.
- In-memory resource list and create endpoint.

### 04_models
Folder: [04_models/](../04_models/)
- Present as a curriculum slot for model-focused examples.
- Currently empty in this workspace snapshot.

### 05_envVariables
File: [05_envVariables/app.py](../05_envVariables/app.py)
- Loading configuration from environment variables.
- Settings pattern with BaseSettings.
- Separating secrets/config from code.

### 06_todoApp
Files: [06_todoApp/main.py](../06_todoApp/main.py), [06_todoApp/router/todoRouter.py](../06_todoApp/router/todoRouter.py), [06_todoApp/middlewares/loggingmiddleware.py](../06_todoApp/middlewares/loggingmiddleware.py)
- Modular app structure (routers, services, schemas, middlewares, exceptions).
- JSON-file backed CRUD services.
- Custom exception handling and global error handling.
- Logging middleware and content negotiation (JSON to XML).
- Health and metrics style endpoints.

### 07_middleware
File: [07_middleware/app.py](../07_middleware/app.py)
- Middleware pipeline behavior.
- Request/response interception.
- Cross-cutting concerns examples: security, logging, masking/PII commentary.

### 08_rdbms
Files: [08_rdbms/main.py](../08_rdbms/main.py), [08_rdbms/README.md](../08_rdbms/README.md)
- FastAPI + SQLAlchemy integration with PostgreSQL.
- Dependency injection for DB session with Depends.
- CRUD endpoints backed by relational storage.
- Pagination, error handling, and health checks.
- Project layout suitable for real service implementations.

### 09_DI
File: [09_DI/main.py](../09_DI/main.py)
- Dependency injection concept via strategy interface.
- Runtime behavior switching through env vars.
- Dynamic module/class loading with importlib.
- Example algorithms (sorting/searching) to demonstrate loose coupling.

### 10_exercise
Files: [10_exercise/task.md](../10_exercise/task.md), [10_exercise/task3.md](../10_exercise/task3.md), [10_exercise/02_task_refactored/app.py](../10_exercise/02_task_refactored/app.py)
- Hands-on API design exercises.
- Versioned endpoint implementation and refactoring.
- OpenAPI customization.
- End-to-end assignment requirements: middleware, services, schemas, exception handling, health/metrics, persistence.
- Advanced assignment: unified API layer over AWS AI services (Comprehend, Textract, Rekognition, Translate, Polly, optional Bedrock).

## Suggested Teaching Sequence
1. Foundations: microservices, HTTP, JSON, REST.
2. FastAPI basics and routing: 01_basic -> 02_router.
3. Contract-first API design: 03_schemas.
4. Configuration and middleware: 05_envVariables -> 07_middleware.
5. Applied modular service: 06_todoApp.
6. RDBMS integration and production patterns: 08_rdbms.
7. DI and extensibility concepts: 09_DI.
8. Practice and capstone-style exercises: 10_exercise.
