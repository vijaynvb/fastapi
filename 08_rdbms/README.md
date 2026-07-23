# FastAPI Todo CRUD Application

A complete FastAPI application demonstrating CRUD (Create, Read, Update, Delete) operations with PostgreSQL database integration.

## Project Structure

```
08_rdbms/
├── main.py                  # FastAPI application with endpoints
├── requirements.txt         # Project dependencies
├── test_main.py            # Comprehensive test suite
├── db/
│   └── postgresql.py       # Database configuration and session management
├── models/
│   └── Todo.py             # SQLAlchemy ORM model
├── schemas/
│   └── todoschema.py       # Pydantic request/response schemas
└── services/
    └── dbpgservice.py      # Business logic for CRUD operations
```

## Features

- ✅ **Create**: Add new todos to the database
- ✅ **Read**: Retrieve todos (single or all with pagination)
- ✅ **Update**: Modify existing todos (full or partial updates)
- ✅ **Delete**: Remove todos from the database
- ✅ **Validation**: Request validation using Pydantic schemas
- ✅ **Error Handling**: Comprehensive HTTP error responses
- ✅ **Testing**: Full test coverage with pytest

## Installation & Setup

### 1. Create Virtual Environment

```bash
cd 08_rdbms
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Database Setup

Update the PostgreSQL connection string in `db/postgresql.py`:

```python
SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost:5432/todo_db"
```

Ensure PostgreSQL is running and create the database:

```sql
CREATE DATABASE todo_db;
```

## Running the Application

### Start the Server

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Access API Documentation

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## API Endpoints

### Health Check

```http
GET /health
```

### Create Todo

```http
POST /todos
Content-Type: application/json

{
  "title": "Buy groceries",
  "description": "Buy milk, eggs, and bread",
  "completed": false
}
```

**Response**: `201 Created`

```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Buy milk, eggs, and bread",
  "completed": false
}
```

### Get Single Todo

```http
GET /todos/{todo_id}
```

**Response**: `200 OK`

```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Buy milk, eggs, and bread",
  "completed": false
}
```

### Get All Todos (with Pagination)

```http
GET /todos?skip=0&limit=10
```

**Response**: `200 OK`

```json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "description": "Buy milk, eggs, and bread",
    "completed": false
  },
  {
    "id": 2,
    "title": "Complete project",
    "description": "Finish FastAPI project",
    "completed": true
  }
]
```

### Update Todo

```http
PUT /todos/{todo_id}
Content-Type: application/json

{
  "title": "Updated title",
  "description": "Updated description",
  "completed": true
}
```

Partial updates are supported:

```json
{
  "completed": true
}
```

**Response**: `200 OK`

### Delete Todo

```http
DELETE /todos/{todo_id}
```

**Response**: `204 No Content`

---

## Key Implementation Details

1. **Dependency Injection**: Uses FastAPI's `Depends()` for database session management
2. **Transaction Management**: Automatic commit/rollback with SQLAlchemy ORM
3. **Pagination**: Supports `skip` and `limit` query parameters
4. **Partial Updates**: Update endpoint supports partial payload (None fields are ignored)
5. **Error Handling**: Proper HTTP status codes (201, 404, etc.) and error messages
6. **Type Safety**: Full type hints throughout the codebase
7. **Testing**: Uses SQLite in-memory database for fast, isolated tests

## Troubleshooting

### Database Connection Error

Ensure PostgreSQL is running and the connection string is correct:

```bash
# Test PostgreSQL connection
psql postgresql://username:password@localhost:5432/todo_db
```

### Port Already in Use

If port 8000 is already in use:

```bash
uvicorn main:app --reload --port 8001
```

### Module Import Errors

Ensure all files are in the correct directory structure and the virtual environment is activated.
