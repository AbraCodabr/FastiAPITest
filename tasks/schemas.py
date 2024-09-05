from pydantic import BaseModel

class Tasks(BaseModel):
    name: str
    description: str