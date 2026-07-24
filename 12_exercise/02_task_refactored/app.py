from fastapi import APIRouter, FastAPI
from fastapi.openapi.utils import get_openapi
from v1.endpoints import global_router_v1
from v2.endpoints import global_router_v2
import uvicorn

app = FastAPI()

app.include_router(global_router_v1)
app.include_router(global_router_v2)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="2.5.0",
        summary="This is a very custom OpenAPI schema",
        description="Here's a longer description of the custom **OpenAPI** schema",
        routes=app.routes,
    )
    # Add custom branding (logo in docs)
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi