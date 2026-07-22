from fastapi import FastAPI

app = FastAPI(
    title="My API",
    description="This is a sample API",
    version="1.0.0",
    root_path="/api/v1"
)

@app.middleware("http")
async def add_custom_header_2(request, call_next):
    print("middleware 2 executed request path:")
    response = await call_next(request)
    print("middleware 2 executed response path:")
    return response

@app.middleware("http")
async def security_middleware(request, call_next):
    print("security middleware executed request path:")
    response = await call_next(request)
    return response

@app.middleware("http")
async def PII_response(request, call_next):
    response = await call_next(request)
    print("PII middleware executed response path: mask the resonse data to hide the PII data")
    return response

@app.middleware("http")
async def logging_response(request, call_next):
    response = await call_next(request)
    print("middleware 1 executed response path:")
    return response

#app.add_middleware(HTTPSRedirectMiddleware)

@app.get("/")
def read_root():
    print("root method executed")
    return {"Hello": "world"}