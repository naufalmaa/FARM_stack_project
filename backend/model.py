from pydantic import BaseModel
# for auto json creator

class Todo(BaseModel):
    title: str
    description: str
    