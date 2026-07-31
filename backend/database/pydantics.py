from pydantic import BaseModel
from datetime import datetime

class TodoBase(BaseModel):
    name: str
    description: str | None = None
    model_config = {
        "from_attributes": True
    }

class TodoIn(TodoBase):
    created_at: datetime

class TodoUpdate(TodoBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "My updated name",
                    "description": "My updated description",
                }
            ]
        }
    }

class TodoUpdateOut(TodoBase):
    id: int
    updated_at: datetime
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "name": "My updated name",
                    "description": "My updated description",
                    "updated_at": "YYYY-MM-DD HH:MM:SS"
                }
            ]
        }
    }


class TodoOut(TodoIn):
    id: int
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "name": "My first todo",
                    "description": "This is a description",
                    "created_at": "YYYY-MM-DD HH:MM:SS"
                }
            ]
        }
    }

