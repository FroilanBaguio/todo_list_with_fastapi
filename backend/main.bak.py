import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from database import models, todo, engine
from sqlalchemy.orm import Session
from typing import List

app = FastAPI()

models.Base.metadata.create_all(bind=engine.engine)

def db_session():
    try:
        db = engine.SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/", tags=["GET"], response_model=List[todo.TodoIn])
@app.get("/todo", tags=["GET"], response_model=List[todo.TodoIn])
async def index(db: Session = Depends(db_session)):
    query = db.query(models.Todo).all()
    if len(query) <= 0:
        raise HTTPException(status_code=404, detail="No todo found")
    return query

@app.get("/todo/{todo_id}/", tags=["GET"], response_model=todo.TodoIn)
async def get_todo(todo_id: int, db: Session = Depends(db_session)):
    query = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="Todo not found")
    return query

@app.post("/todo/", tags=["POST"], response_model=todo.TodoIn)
async def create_todo(todo: todo.TodoIn, db: Session = Depends(db_session)) -> todo.TodoIn:
    todo = models.Todo(
        title = todo.title,
        description = todo.description
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

@app.put("/todo/{todo_id}/update", tags=["UPDATE"], response_model=todo.TodoOut)
async def update_todo(todo_id: int, todo: todo.TodoOut, db: Session = Depends(db_session)) -> todo.TodoOut:
    t1 = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not t1:
        raise HTTPException(status_code=404, detail="Todo not found")
    t1.title = todo.title
    t1.description = todo.description
    db.commit()
    query = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    #return db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    return query

@app.delete("/todo/{todo_id/delete", tags=["DELETE"])
async def delete_todo(todo_id: int, db: Session = Depends(db_session)):
    try:
        db.query(models.Todo).filter(models.Todo.id == todo_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
    return {"status": "success"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
