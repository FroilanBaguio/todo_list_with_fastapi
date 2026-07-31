from database import models, engine

def create_database() -> None:
    models.Base.metadata.create_all(engine.engine)

def drop_database() -> None:
    models.Base.metadata.drop_all(engine.engine)
