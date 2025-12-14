class Student:
    def __init__(self, name: str, age: int, score: float):
        self.name = name
        self.age = age
        self.score = score

    def is_passed(self) -> bool:
        """Đậu nếu điểm >= 5"""
        return self.score >= 5

    def __str__(self) -> str:
        return f"{self.name} ({self.age} tuổi) – Điểm: {self.score}"
