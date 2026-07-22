from fastapi.responses import JSONResponse
class TodoNotFoundException(Exception):
    def __init__(self, todo_id: int):
        self.todo_id = todo_id
        self.message = f"Todo with ID {todo_id} not found."
        super().__init__(self.message)

def todo_not_found_exception_handler(request, exc: TodoNotFoundException):
    return JSONResponse(
        status_code=204,
        content={"message": exc.message},
    )