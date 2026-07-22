import json
from xml.etree.ElementTree import Element, SubElement, tostring

from fastapi import APIRouter, FastAPI
from fastapi.responses import HTMLResponse, Response
from router.todoRouter import todo_router_v1
from router.userRouter import user_router_v1

# httpclient, ftpclient, smtpclient 

app = FastAPI(title="Todo App")


def _build_xml(parent: Element, value):
    if isinstance(value, dict):
        for key, child_value in value.items():
            child = SubElement(parent, str(key))
            _build_xml(child, child_value)
        return

    if isinstance(value, list):
        for item in value:
            child = SubElement(parent, "item")
            _build_xml(child, item)
        return

    parent.text = "" if value is None else str(value)


def _json_to_xml_bytes(data) -> bytes:
    root = Element("response")
    _build_xml(root, data)
    return tostring(root, encoding="utf-8", xml_declaration=True)


async def _read_response_body_bytes(response) -> bytes:
    if hasattr(response, "body") and response.body is not None:
        return response.body

    body_chunks = [chunk async for chunk in response.body_iterator]
    return b"".join(body_chunks)

# enable content negotiation for all routes in the application as middleware
@app.middleware("http")
async def content_negotiation_middleware(request, call_next):
    # Keep built-in OpenAPI/Swagger endpoints unchanged.
    if request.url.path.startswith(("/docs", "/openapi.json", "/redoc")):
        return await call_next(request)

    response = await call_next(request)

    accept_header = request.headers.get("accept", "").lower()
    wants_xml = "application/xml" in accept_header
    if not wants_xml:
        return response

    response_media_type = (getattr(response, "media_type", "") or "").lower()
    content_type_header = (response.headers.get("content-type", "") or "").lower()
    is_json_response = "application/json" in response_media_type or "application/json" in content_type_header
    if not is_json_response:
        return response

    body_bytes = await _read_response_body_bytes(response)
    if not body_bytes:
        return response

    try:
        json_data = json.loads(body_bytes)
    except json.JSONDecodeError:
        return response

    xml_body = _json_to_xml_bytes(json_data)
    passthrough_headers = {
        key: value
        for key, value in response.headers.items()
        if key.lower() not in {"content-length", "content-type"}
    }

    return Response(
        content=xml_body,
        status_code=response.status_code,
        headers=passthrough_headers,
        media_type="application/xml",
    )

    return response

global_router_v1 = APIRouter(prefix="/api/v1")
global_router_v1.include_router(todo_router_v1)
global_router_v1.include_router(user_router_v1)
app.include_router(global_router_v1)