from fastapi import FastAPI, Request
from routers import todoRouter
from routers import authRouter  # add this import
from routers import userRouter
from error.todoNotFound import todo_not_found_exception_handler, TodoNotFoundException
from error.userNotFound import user_not_found_exception_handler, UserNotFoundException

app = FastAPI(title="Todo App", version="1.0.0", description="Todo application API")

app.include_router(authRouter.router, prefix="/auth", tags=["auth"])
app.include_router(userRouter.router, prefix="/users", tags=["users"])
app.include_router(todoRouter.router, prefix="/todos", tags=["todos"])

app.add_exception_handler(TodoNotFoundException, todo_not_found_exception_handler)
app.add_exception_handler(UserNotFoundException, user_not_found_exception_handler)
