from fastapi import FastAPI, status, Depends, params
from fastapi.encoders import jsonable_encoder
import asyncio
import psutil
import datetime
import json
import pytest
from model import Creature

app = FastAPI()

@app.get("/async")
async def greet():
    await asyncio.sleep(1)
    return "Hello? Async?"

@app.get("/hi/{who}")
def greet(who):
    return f"Hello? {who}?"

@app.get("/happy", status_code=status.HTTP_201_CREATED)
def happy():
    return "#"

@app.get("/creature")
def get_all() -> list[Creature]:
    from data import get_creatures
    return get_creatures()

@app.get("/top")
def top():
    return f"CPU:\n {psutil.cpu_times()}"


@pytest.fixture
def data():
    return datetime.datetime.now()

def test_json_dump(data):
    with pytest.raises(Exception):
        _ = json.dumps(data)

def test_encoder(data):
    out = jsonable_encoder(data)
    assert out
    json_out = json.dumps(out)
    assert json_out


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("web:app", reload=True)