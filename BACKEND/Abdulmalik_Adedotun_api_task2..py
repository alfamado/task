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

class PatchItem(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    track: Optional[str] = None

@app.patch("/edit-data/{id}")
def edit_data(id: int, req: PatchItem):
    try:
        existing = data[id]
    except IndexError:
        return {"Message": "Record not found"}

    try:
        updates = req.model_dump(exclude_unset=True)
    except AttributeError:
        updates = req.model_dump(exclude_unset=True)

    if updates:
        existing.update(updates)
        data[id] = existing
        print(data)
        return {"Message": "Data edited", "Data": data}
    else:
        return {"Message": "No fields to update", "Data": data}
    
@app.delete("/delete-data/{id}")
def delete_data(id: int):
    try:
        del data[id]
        print(data)
        return {"Message": "Data Deleted", "Data": data}
    except IndexError:
        return {f"Message": "Record not found"}

if __name__ == "__main__":
    print(os.getenv("host"))
    print(os.getenv("port"))
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")))