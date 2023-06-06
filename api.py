import fastapi
import uvicorn

app = fastapi.FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, World"}

@app.get("/summary")
def summary():
    return {"message": "summary from the textb given"}
