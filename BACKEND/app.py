from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import uvicorn
import os
from typing import Optional

load_dotenv()

app = FastAPI(title="simple FastAPI", version="1.0.0")
data = [{"name": "Raimi Abass", "age": 26, "track": "System Analyst"},
        {"name": "Abdulmalik Adedotun", "age": 32, "track": "AI Engineer"},
        {"name": "Joy Adeyemi", "age": 25, "track": "Frontend Developer"}]

class Item(BaseModel):
    name: str = Field(..., example="Perpetual")
    age: int = Field(..., example=25)
    track: str = Field(..., example="Frontend Developer")

@app.get("/", description = "This endpoint just returns a welcome message")
def root():
    return {"Message": "Welcome to my FastAPI Application"}

@app.get("/get-data")
def get_data():
    return data

@app.post("/create")
def create_data(req: Item):
    data.append(req.dict())
    print(data)
    return {"Message": "Data Received", "Data": data}

@app.put("/update_data/{id}")
def update_data(id: int, req: Item):
    data[id] = req.dict()
    print(data)
    return {"Message": "Data Updated", "Data": data}

if __name__ == "__main__":
    print(os.getenv("host"))
    print(os.getenv("port"))
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")))