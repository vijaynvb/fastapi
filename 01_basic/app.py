from fastapi import FastAPI
import uvicorn 

app = FastAPI(
    title="My API",
    description="This is a sample API",
    version="1.0.0",
    root_path="/api/v1"
)

@app.get("/")
def read_root():
    return {"Hello": "world"}


@app.get("/employees/{id}")
# validation framwork errors
def read_item(id: int):
    return {"id": id}

@app.get("/employees/{id}/departments/{deptid}")
# validation framwork errors
def read_item(id: int, deptid: int):
    return {"id": id, "deptid": deptid}

# /employees?pageno=1&limit=10

@app.get("/employees")
def read_item(pageno: int = 1, limit: int = 10 ):
    return {"pageno": pageno, "limit": limit}

if __name__ =="__main__":
    uvicorn.run(app,host="localhost", port=5000)

    