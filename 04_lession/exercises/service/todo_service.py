from fastapi import HTTPException
from typing import Optional
from models.todo import TodoCreate, TodoUpdate

_todos: list[dict] = []
_id_counter = 1


def _is_title_exists(title: str, exclude_id: Optional[int] = None) -> bool:
    for todo in _todos:
        if exclude_id is not None and todo["id"] == exclude_id:
            continue
        if todo["title"].lower() == title.lower():
            return True
    return False


def create_todo(data: TodoCreate) -> dict:
    global _id_counter

    if _is_title_exists(data.title):
        raise HTTPException(
            status_code=409,
            detail="Todo title already exists"
        )

    todo = {
        "id": _id_counter,
        **data.model_dump()
    }
    _id_counter += 1
    _todos.append(todo)
    return todo


def get_all_todos(
    done: Optional[bool],
    keyword: Optional[str],
    limit: int
) -> list[dict]:
    result = _todos

    if done is not None:
        result = [t for t in result if t["done"] == done]

    if keyword:
        kw = keyword.lower()
        result = [t for t in result if kw in t["title"].lower()]

    return result[:limit]


def get_todo_by_id(todo_id: int) -> Optional[dict]:
    return next((t for t in _todos if t["id"] == todo_id), None)


def update_todo_put(todo_id: int, data: TodoCreate) -> Optional[dict]:
    todo = get_todo_by_id(todo_id)
    if not todo:
        return None

    if _is_title_exists(data.title, exclude_id=todo_id):
        raise HTTPException(
            status_code=409,
            detail="Todo title already exists"
        )

    todo.update(data.model_dump())
    return todo


def update_todo_patch(todo_id: int, data: TodoUpdate) -> Optional[dict]:
    todo = get_todo_by_id(todo_id)
    if not todo:
        return None

    if data.title and _is_title_exists(data.title, exclude_id=todo_id):
        raise HTTPException(
            status_code=409,
            detail="Todo title already exists"
        )

    for k, v in data.model_dump(exclude_unset=True).items():
        todo[k] = v

    return todo


def delete_todo(todo_id: int) -> bool:
    global _todos
    for i, todo in enumerate(_todos):
        if todo["id"] == todo_id:
            _todos.pop(i)
            return True
    return False
