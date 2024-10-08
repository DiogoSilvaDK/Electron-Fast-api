from fastapi import FastAPI
import api_model
import os
from test_api import get_weather

HOST = "127.0.0.1"
PORT = 7777

app = FastAPI()

@app.get("/hello/{name}")
def read_root(name: str):
    result = get_weather(name)
    return result

@app.post("/open-explorer/")
def open_explorer(model: api_model.PathModel):
    
    os.startfile(model.path)

    return f"Opening {model.path}"

if __name__ == "__main__":
    import asyncio
    import uvicorn

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(uvicorn.run(app, host=HOST, port=PORT))