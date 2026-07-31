from datetime import datetime
from pydantic import BaseModel, EmailStr

class TodoBase(BaseModel):
    title: str
    description: str

    model_config = {
        "from_attributes": True,
    }

class TodoIn(TodoBase):
    created_at: datetime
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "First Todo",
                    "description": "This is my first todo list, I am so happy!", 
                    "created_at": "YYYY-MM-DD HH:MM:SS"
                }
            ]
        }
    }

class TodoOut(TodoBase):
    updated_at: datetime
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "First Todo",
                    "description": "This is my first todo list, I am so happy!", 
                    "updated_at": "YYYY-MM-DD HH:MM:SS"
                }
            ]
        }
    }

