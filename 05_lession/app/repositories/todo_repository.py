from sqlalchemy import select, func
from sqlalchemy.orm import Session
from .base_repository import BaseRepository
from app.models.todo import Todo


class TodoRepository(BaseRepository[Todo]):
    def __init__(self):
        super().__init__(Todo)

    def get_by_title(self, db: Session, title: str) -> Todo | None:
        return db.query(Todo).filter(func.lower(Todo.title) == title.lower()).first()

    def search(
        self,
        db: Session,
        *,
        done: bool = None,
        keyword: str = None,
        offset: int = 0,
        limit: int = 10,
    ):
        query = db.query(Todo)
        if done is not None:
            query = query.filter(Todo.done == done)
        if keyword:
            query = query.filter(Todo.title.ilike(f"%{keyword}%"))

        return query.offset(offset).limit(limit).all()
