import uvicorn
from fastapi import FastAPI, Depends, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Annotated, List
# below is for database connection and operation
from database import models, engine, utils, operations, pydantics
from sqlalchemy import text
from sqlalchemy.orm import Session
from uuid import UUID

app = FastAPI()

#utils.drop_database()
utils.create_database()
# with engine.engine.connect() as conn:
#     result = conn.execute(text("SELECT 'hello, world'"))
#     print(result.all())
#     conn.commit()
#     v then select the texts then gc to comment it all at once

class FilterParams(BaseModel):
    skip: int = Field(0, ge=0, le=100)
    limit: int = Field(10, gt=0, le=100)

@app.get("/", tags=["GET"], response_model=List[pydantics.TodoOut])
@app.get("/todo", tags=["GET"], response_model=List[pydantics.TodoOut])
async def index(filter_query: Annotated[FilterParams, Query()]):
    return operations.read_todo()[filter_query.skip: filter_query.skip + filter_query.limit]

@app.post("/todo/create", tags=["POST"], response_model=pydantics.TodoOut)
async def create_todo(todo: pydantics.TodoIn) -> pydantics.TodoIn:
    return operations.create_todo(todo.name, todo.description)

# below is for fetching a todo base on it's id
@app.get("/todo/{todo_id}", tags=["GET"], response_model=pydantics.TodoOut)
async def select_todo(todo_id: int):
    return operations.select_todo(todo_id)

@app.put("/todo/{todo_id}/update", tags=["UPDATE"], response_model=pydantics.TodoUpdateOut)
async def update_todo(todo_id: int, todo: pydantics.TodoUpdate):
    return operations.update_todo(todo_id, todo.name, todo.description)

@app.delete("/todo/{todo_id}/delete", tags=["DELETE"])
async def delete_todo(todo_id: int):
    operations.delete_todo(todo_id)
    return {"status": "sucessfully delete a todo"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
