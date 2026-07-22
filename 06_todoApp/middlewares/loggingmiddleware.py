from utils.logging_config import setup_logging
from datetime import datetime
import time
import uuid
from fastapi import Request
logger = setup_logging()
startup_time = datetime.utcnow()

async def log_requests(request: Request, call_next):
    request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
    start = time.perf_counter()
    client = request.client.host if request.client else "unknown"
    method = request.method
    path = request.url.path

    logger.info(f"[{request_id}] -> {client} {method} {path}")
    try:
        response = await call_next(request)
    except Exception as ex:
        duration_ms = (time.perf_counter() - start) * 1000
        logger.exception(f"[{request_id}] !! {method} {path} failed in {duration_ms:.2f}ms: {ex}")
        raise
    duration_ms = (time.perf_counter() - start) * 1000
    logger.info(f"[{request_id}] <- {method} {path} {response.status_code} {duration_ms:.2f}ms")
    response.headers["X-Request-ID"] = request_id
    response.headers["X-Process-Time-ms"] = f"{duration_ms:.2f}"
    return response