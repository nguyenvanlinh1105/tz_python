from typing import Any
# BTTH7: Thông tin sinh viên
student: dict[str, Any] = {
    "name": "Nguyen Van A",
    "age": 20,
    "scores": [7.5, 8.0, 6.5, 9.0],
}


print("Name :", student["name"])
print("Age :", student["age"])
student["avg_score"] = sum(student["scores"]) / len(student["scores"])
print("Average score :", student["avg_score"])

# BTTH8: Đếm tần suất xuất hiện ký tự

s = "hello world"
counter = {}
for c in s:
    counter[c] = counter.get(c, 0) + 1

print(counter)

# BTTH9: Quản lý danh sách sinh viên bằng dict
students: dict[str, dict[str, Any]] = {
    "SV01": {"name": "Nguyen Van A", "age": 20},
    "SV02": {"name": "Tran Thi B", "age": 21},
}

students["SV03"] = {}
students["SV03"]["age"] = 23

print(students)


