# Bài tập 1: Quản lý học viên & khóa học
# Danh sách học viên (list các tuple)
students = [
    ("SV01", "Nguyen Van A", 20),
    ("SV02", "Tran Thi B", 21),
    ("SV03", "Le Van C", 19),
]

# Dict lưu điểm từng môn cho từng sinh viên
scores = {
    "SV01": {"math": 8.0, "python": 7.5},
    "SV02": {"math": 6.5, "python": 8.5},
    "SV03": {"math": 9.0, "python": 9.5},
}

# Set các môn học hiện có
courses = {"math", "python"}

# Yêu cầu:
# a. Dùng vòng lặp + unpacking tuple để in ra danh sách học viên theo format
#     SV01 - Nguyen Van A (20)
#     SV02 - Tran Thi B (21)
#     ...
# b. Tạo một list mới python_scores chỉ chứa tuple (student_id, name, python_score)
# c. Tìm học viên có điểm Python cao nhất từ python_scores và in ra: Top Python: <name> - <score>
# d. Thêm môn mới "database" vào courses (dùng set) và gán tạm điểm database = 0 cho tất cả sinh viên trong scores


# 1.a
print("BÀI TẬP 1.a")
for masv, name, age in students:
    print(f"{masv} - {name} - {age}")

# 1.b
print("BÀI TẬP 1.b")
python_courses = []

for masv, name, age in students:
    python_score = scores.get(masv).get("python")
    python_courses.append((masv, name, python_score))

print(python_courses)

#1.c
print("BÀI TẬP 1.c")
max_score = None
tops = []
for masv, name, score in python_courses:
    if max_score is None or score > max_score:
        max_score = score
        tops = [(masv, name, score)]
    elif score == max_score:
        tops.append((masv, name, score))

if not tops:
    print("Không có học viên nào.")
elif len(tops) == 1:
    _, name, score = tops[0]
    print(f"Top Python: {name} - {score}")
else:
    print("Top Python (tie):")
    for _, name, score in tops:
        print(f"- {name} - {score}")
#1.d
print("BÀI TẬP 1.d")
courses.add("database")

for masv in scores:
    scores.get(masv)["database"] = 0

print(scores)
