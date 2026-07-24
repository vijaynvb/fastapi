# service to perform database CRUD operations on PostgreSQL database
from sqlalchemy.orm import Session
from models.Todo import Todo
from schemas.todoschema import TodoCreate, TodoUpdate


class TodoService:
    """Service class to perform CRUD operations on Todo model"""

    def create_todo(db: Session, todo: TodoCreate) -> Todo:
        """Create a new todo in the database"""
        db_todo = Todo(
            title=todo.title,
            description=todo.description,
            completed=1 if todo.completed else 0,
        )
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return db_todo

    def get_todo(db: Session, todo_id: int) -> Todo:
        """Get a todo by id"""
        return db.query(Todo).filter(Todo.id == todo_id).first()

    def get_all_todos(db: Session, skip: int = 0, limit: int = 10) -> list:
        """Get all todos with pagination"""
        return db.query(Todo).offset(skip).limit(limit).all()

    def update_todo(db: Session, todo_id: int, todo_update: TodoUpdate) -> Todo:
        """Update a todo by id"""
        db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
        if db_todo:
            if todo_update.title is not None:
                db_todo.title = todo_update.title
            if todo_update.description is not None:
                db_todo.description = todo_update.description
            if todo_update.completed is not None:
                db_todo.completed = 1 if todo_update.completed else 0
            db.commit()
            db.refresh(db_todo)
        return db_todo

    def delete_todo(db: Session, todo_id: int) -> bool:
        """Delete a todo by id"""
        db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
        if db_todo:
            db.delete(db_todo)
            db.commit()
            return True
        return False
