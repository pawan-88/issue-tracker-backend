from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    model: str


class ProjectCreate(BaseModel):
    name : str
    description: str
    created_by: int

class IssueCreated(BaseModel):
    title:str
    description: str
    priority : str
    project_id : int
    assigned_to: Optional[int]

class CommentCreate(BaseModel):
    user_id: int
    message: str