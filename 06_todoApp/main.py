import json
from fastapi import APIRouter, FastAPI
from middlewares.jsontoxmlmiddleware import content_negotiation_middleware
from middlewares.loggingmiddleware import log_requests as logging_middleware
from router.todoRouter import todo_router_v1
from router.userRouter import user_router_v1
from router.healthRouter import metrics_router

# httpclient, ftpclient, smtpclient 

app = FastAPI(title="Todo App")


# enable content negotiation for all routes in the application as middleware

app.middleware("http")(logging_middleware)
app.middleware("http")(content_negotiation_middleware)

global_router_v1 = APIRouter(prefix="/api/v1")
global_router_v1.include_router(todo_router_v1)
global_router_v1.include_router(user_router_v1)
global_router_v1.include_router(metrics_router)
app.include_router(global_router_v1)

@app.get("/health",tags=["Metrics"], summary="Get Health of Application", description="Get Health of Application")
def read_health():
    return {"health": "ok"}