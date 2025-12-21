from fastapi import APIRouter, Query, HTTPException, status
from typing import Optional, List
from models.todo import TodoCreate, TodoUpdate, TodoOut
from service.todo_service import (
    create_todo,
    get_all_todos,
    get_todo_by_id,
    update_todo_put,
    update_todo_patch,
    delete_todo,
)

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.post("", response_model=TodoOut, status_code=status.HTTP_201_CREATED)
def create(data: TodoCreate):
    return create_todo(data)


@router.get("", response_model=List[TodoOut])
def list_todos(
    done: Optional[bool] = Query(default=None, description="Filter by done status"),
    keyword: Optional[str] = Query(
        default=None, description="Search by title"
    ),
    limit: int = Query(
        default=10, ge=1, le=50, description="Limit number of todos"
    ),
):
    return get_all_todos(done, keyword, limit)


@router.get("/{todo_id}", response_model=TodoOut)
def get(todo_id: int):
    todo = get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/{todo_id}", response_model=TodoOut)
def update_put(todo_id: int, data: TodoCreate):
    todo = update_todo_put(todo_id, data)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.patch("/{todo_id}", response_model=TodoOut)
def update_patch(todo_id: int, data: TodoUpdate):
    todo = update_todo_patch(todo_id, data)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(todo_id: int):
    success = delete_todo(todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
