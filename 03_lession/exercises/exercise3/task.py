from datetime import datetime


class Task:
    def __init__(self, description: str, due_date: datetime, status: str = "todo"):
        self.description = description
        self.due_date = due_date
        self.status = status  # "todo" hoặc "done"

    # Trả về True nếu quá hạn và chưa done
    def is_overdue(self, now: datetime) -> bool:
        return self.status == "todo" and self.due_date < now

    def __str__(self) -> str:
        status_text = "TODO" if self.status == "todo" else "DONE"
        return f"[{status_text}] {self.description} (Hạn: {self.due_date.strftime('%Y-%m-%d')})"
