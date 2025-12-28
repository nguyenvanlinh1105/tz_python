from typing import Generic, TypeVar, Optional
from pydantic import BaseModel

T = TypeVar("T")


class SuccessResponse(BaseModel, Generic[T]):
    trace_id: Optional[str] = None
    data: Optional[T] = None
    message: str = "Success"

    model_config = {"from_attributes": True}
