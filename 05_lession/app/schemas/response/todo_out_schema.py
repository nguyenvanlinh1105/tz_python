from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TodoOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    priority: int
    done: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
