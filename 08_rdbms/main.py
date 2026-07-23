# Main entry point for the FastAPI application
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.postgresql import init_db, get_db
from models.Todo import Todo
from schemas.todoschema import Todo as TodoSchema, TodoCreate, TodoUpdate
from services.dbpgservice import TodoService

app = FastAPI(title="Todo API", version="1.0.0")

# Initialize the database
init_db()


# CRUD Endpoints
@app.post("/todos", response_model=TodoSchema, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    """Create a new todo"""
    return TodoService.create_todo(db, todo)


@app.get("/todos/{todo_id}", response_model=TodoSchema)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    """Get a todo by id"""
    todo = TodoService.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found"
        )
    return todo


@app.get("/todos", response_model=list[TodoSchema])
def get_all_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Get all todos with pagination"""
    return TodoService.get_all_todos(db, skip, limit)


@app.put("/todos/{todo_id}", response_model=TodoSchema)
def update_todo(todo_id: int, todo_update: TodoUpdate, db: Session = Depends(get_db)):
    """Update a todo by id"""
    todo = TodoService.update_todo(db, todo_id, todo_update)
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found"
        )
    return todo


@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """Delete a todo by id"""
    if not TodoService.delete_todo(db, todo_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found"
        )
    return None


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
