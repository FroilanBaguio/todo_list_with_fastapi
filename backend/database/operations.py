from sqlalchemy.orm import Session
from database import engine, models
from sqlalchemy import select

# below uses orm
def create_todo(name: str, description: str) -> None:
    with Session(engine.engine) as session:
        todo = models.Todo(name=name, description=description)
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return todo

# below uses core
def read_todo() -> None:
    with Session(engine.engine) as session:
        query = select(models.Todo)
        result = session.scalars(query)
        return result.all()

def select_todo(id: int) -> None:
    with Session(engine.engine) as session:
        query = select(models.Todo).where(models.Todo.id == id)
        result = session.scalars(query)
        return result.first()

def update_todo(id: int, name: str, description: str) -> None:
    with Session(engine.engine) as session:
        query = select(models.Todo).where(models.Todo.id == id)
        result = session.scalars(query)
        todo = result.first()
        todo.name = name
        todo.description = description
        session.commit()
        session.refresh(todo)
        return todo

def delete_todo(id: int) -> None:
    with Session(engine.engine) as session:
        query = session.get(models.Todo, id)
        session.delete(query)
        session.commit()

# querying guide: https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html
# result = session.execute(select(User).order_by(User.id))
# result.all()

# below is for order_by
# stmt = select(Manager).order_by(Manager.id)
# managers = session.scalars(stmt).all()
