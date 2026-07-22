from fastapi import APIRouter
import os
metrics_router = APIRouter(prefix="/metrics", tags=["Metrics"])

@metrics_router.get("/cpu",tags=["Metrics"], summary="Get Health of Application", description="Get Health of Application")
def read_cpu():
    cpu_usage = os.getloadavg()[0]  # 1-minute load average
    return {"cpu": cpu_usage}


@metrics_router.get("/mem",tags=["Metrics"], summary="Get Memory Usage of Application", description="Get Memory Usage of Application")
def read_mem():
    mem_usage = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')  # Total physical memory in bytes
    return {"mem": mem_usage}