from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.todo_repository import TodoRepository
from app.models.todo import Todo
from app.schemas.request.todo_schema import TodoCreate, TodoUpdate


class TodoService:
    def __init__(self):
        self.repo = TodoRepository()

    def create_todo(self, db: Session, data: TodoCreate):
        if self.repo.get_by_title(db, data.title):
            raise HTTPException(status_code=409, detail="Title already exists")
        if not (1 <= data.priority <= 5):
            raise HTTPException(status_code=400, detail="Priority must be 1-5")
        new_todo = Todo(**data.model_dump())
        todo = self.repo.create(db, new_todo)
        db.commit()
        db.refresh(todo)
        return todo

    def get_todo(self, db: Session, todo_id: int):
        todo = self.repo.get_by_id(db, todo_id)
        if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        return todo

    def list_todos(self, db: Session, done=None, keyword=None, offset=0, limit=10):
        return self.repo.search(
            db, done=done, keyword=keyword, offset=offset, limit=limit
        )

    def update_todo_put(self, db: Session, todo_id: int, data: TodoCreate):
        todo = self.get_todo(db, todo_id)
        check_title = self.repo.get_by_title(db, data.title)
        if check_title and check_title.id != todo_id:
            raise HTTPException(status_code=409, detail="Title already exists")
        if not (1 <= data.priority <= 5):
            raise HTTPException(status_code=400, detail="Priority must be 1-5")
        todo.title = data.title
        todo.description = data.description
        todo.priority = data.priority
        todo.done = data.done
        db.commit()
        db.refresh(todo)
        return todo

    def update_todo_patch(self, db: Session, todo_id: int, data: TodoUpdate):
        todo = self.get_todo(db, todo_id)
        partial = data.model_dump(exclude_unset=True)
        if "title" in partial:
            check_title = self.repo.get_by_title(db, partial["title"])
            if check_title and check_title.id != todo_id:
                raise HTTPException(status_code=409, detail="Title already exists")
        if "priority" in partial and not (1 <= partial["priority"] <= 5):
            raise HTTPException(status_code=400, detail="Priority must be 1-5")
        for field, value in partial.items():
            setattr(todo, field, value)
        db.commit()
        db.refresh(todo)
        return todo

    def delete_todo(self, db: Session, todo_id: int):
        todo = self.get_todo(db, todo_id)
        db.delete(todo)
        db.commit()
        return None
