from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.todo import Todo


def seed_data():
    """
    Seed initial todo data into the database.
    Only seeds if the database is empty.
    """
    db: Session = SessionLocal()
    try:
        existing_count = db.query(Todo).count()
        if existing_count > 0:
            print(f"Database already has {existing_count} todos. Skipping seed.")
            return

        todos = [
            Todo(
                title="Học FastAPI",
                description="Học CRUD cơ bản với FastAPI và SQLAlchemy",
                priority=5,
                done=False,
            ),
            Todo(
                title="Học Docker",
                description="Build image Postgres và containerize ứng dụng",
                priority=4,
                done=False,
            ),
            Todo(
                title="Học Alembic",
                description="Quản lý database migration với Alembic",
                priority=3,
                done=False,
            ),
            Todo(
                title="Setup môi trường development",
                description="Cài đặt Python, venv, và các dependencies",
                priority=5,
                done=True,
            ),
            Todo(
                title="Viết API documentation",
                description="Tạo Swagger/OpenAPI documentation cho các endpoints",
                priority=2,
                done=False,
            ),
            Todo(
                title="Implement authentication",
                description="Thêm JWT authentication cho API",
                priority=4,
                done=False,
            ),
            Todo(
                title="Unit testing",
                description="Viết unit tests cho services và repositories",
                priority=3,
                done=False,
            ),
            Todo(
                title="Deploy lên production",
                description="Deploy ứng dụng lên cloud server",
                priority=1,
                done=False,
            ),
        ]

        db.add_all(todos)
        db.commit()

    except Exception as e:
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_data()
