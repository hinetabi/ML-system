from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
import uvicorn 
uvicorn.run(app=app, port=8000)