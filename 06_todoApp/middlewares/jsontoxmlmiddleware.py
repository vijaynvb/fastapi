import json
from fastapi.responses import Response
from utils.jsontoxml import _json_to_xml_bytes, _read_response_body_bytes

from fastapi import FastAPI

app = FastAPI()

async def content_negotiation_middleware(request, call_next):
    # Keep built-in OpenAPI/Swagger endpoints unchanged.
    if request.url.path.startswith(("/docs", "/openapi.json", "/redoc")):
        return await call_next(request)
    response = await call_next(request)
    accept_header = request.headers.get("accept", "").lower()
    wants_xml = "application/xml" in accept_header
    if not wants_xml:
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