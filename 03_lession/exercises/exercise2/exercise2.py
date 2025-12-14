from typing import List
from student import Student


def load_students_from_file(filename: str) -> List[Student]:
    students: List[Student] = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()

                if not line:
                    continue

                try:
                    parts = line.split(",")
                    if len(parts) != 3:
                        raise ValueError("Sai số cột")

                    name = parts[0].strip()
                    age = int(parts[1].strip())
                    score = float(parts[2].strip())

                    students.append(Student(name, age, score))

                except ValueError as e:
                    print(f"Dòng {line_number} bị bỏ qua, lỗi: {e}")

    except FileNotFoundError:
        print(f"Không tìm thấy file: {filename}")
    except IOError:
        print("Lỗi không thể đọc file!")

    return students


def calc_avg_score(students: List[Student]) -> float:
    if not students:
        return 0.0

    total_score = sum(s.score for s in students)
    return total_score / len(students)


def find_top_student(students: List[Student]) -> Student | None:
    if not students:
        return None

    top_student = students[0]
    for student in students:
        if student.score > top_student.score:
            top_student = student

    return top_student


def filter_failed(students: List[Student]) -> List[Student]:
    return [s for s in students if not s.is_passed()]


def main():
    while True:
        filename = input(
            "Nhập tên file điểm sinh viên (hoặc 'exit' để thoát): "
        ).strip()

        if filename.lower() == "exit":
            print("Kết thúc chương trình.")
            break

        students = load_students_from_file(filename)

        if not students:
            print("Không có dữ liệu sinh viên hợp lệ.\n")
            continue

        avg_score = calc_avg_score(students)
        top_student = find_top_student(students)
        failed_students = filter_failed(students)

        print(f"Điểm trung bình lớp: {avg_score:.2f}\n")

        if top_student:
            print(f"Sinh viên điểm cao nhất: {top_student}\n")

        print("Danh sách sinh viên bị rớt:")
        if not failed_students:
            print("Không có sinh viên nào rớt.")
        else:
            for student in failed_students:
                print(student)


if __name__ == "__main__":
    main()
