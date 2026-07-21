from fastapi import APIRouter, FastAPI
from v1.endpoints import global_router_v1
from v2.endpoints import global_router_v2
import uvicorn 

app = FastAPI(
    title="My API",
    description="This is a sample API",
    version="1.0.0"
)

app.include_router(global_router_v1)
app.include_router(global_router_v2)