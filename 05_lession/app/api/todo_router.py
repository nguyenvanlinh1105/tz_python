from fastapi import APIRouter, Depends, status, Request
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.request.todo_schema import TodoCreate, TodoUpdate
from app.services.todo_service import TodoService
from app.utils.response_wrapper import SuccessResponse
from app.schemas.response.todo_out_schema import TodoOut

router = APIRouter(prefix="/todos", tags=["Todos"])
todo_service = TodoService()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=SuccessResponse[TodoOut],
    responses={
        409: {"description": "Title already exists"},
        400: {"description": "Invalid priority"},
    },
)
def create(request: Request, data: TodoCreate, db: Session = Depends(get_db)):
    todo = todo_service.create_todo(db, data)
    return SuccessResponse(trace_id=request.state.trace_id, data=todo)


@router.get("/", response_model=SuccessResponse[list[TodoOut]])
def list_todos(
    request: Request,
    done: bool = None,
    keyword: str = None,
    offset: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    items = todo_service.list_todos(db, done, keyword, offset, limit)
    return SuccessResponse(trace_id=request.state.trace_id, data=items)


@router.get(
    "/{todo_id}",
    response_model=SuccessResponse[TodoOut],
    responses={404: {"description": "Todo not found"}},
)
def get(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = todo_service.get_todo(db, todo_id)
    return SuccessResponse(trace_id=request.state.trace_id, data=todo)


@router.put(
    "/{todo_id}",
    response_model=SuccessResponse[TodoOut],
    responses={
        404: {"description": "Todo not found"},
        409: {"description": "Title already exists"},
        400: {"description": "Invalid priority"},
    },
)
def put(
    request: Request, todo_id: int, data: TodoCreate, db: Session = Depends(get_db)
):
    todo = todo_service.update_todo_put(db, todo_id, data)
    return SuccessResponse(trace_id=request.state.trace_id, data=todo)


@router.patch(
    "/{todo_id}",
    response_model=SuccessResponse[TodoOut],
    responses={
        404: {"description": "Todo not found"},
        409: {"description": "Title already exists"},
        400: {"description": "Invalid priority"},
    },
)
def patch(
    request: Request, todo_id: int, data: TodoUpdate, db: Session = Depends(get_db)
):
    todo = todo_service.update_todo_patch(db, todo_id, data)
    return SuccessResponse(trace_id=request.state.trace_id, data=todo)


@router.delete(
    "/{todo_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"description": "Todo not found"}},
)
def delete(todo_id: int, db: Session = Depends(get_db)):
    todo_service.delete_todo(db, todo_id)
    return None
