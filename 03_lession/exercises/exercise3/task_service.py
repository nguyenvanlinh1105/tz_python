from datetime import datetime
from task import Task


def load_tasks(filename: str) -> list[Task]:
    tasks = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=2):
                line = line.strip()
                if not line:
                    continue

                try:
                    description, due_str, status = line.split(";")
                    due_date = datetime.strptime(due_str, "%Y-%m-%d")
                    tasks.append(Task(description, due_date, status))
                except ValueError:
                    print(f"Cảnh báo: Dòng {line_number} sai format, bỏ qua.")
    except FileNotFoundError:
        print("File chưa tồn tại, sẽ tạo mới khi lưu.")

    return tasks


def save_tasks(filename: str, tasks: list[Task]) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        for task in tasks:
            line = f"{task.description};{task.due_date.strftime('%Y-%m-%d')};{task.status}\n"
            file.write(line)


def add_task(tasks: list[Task]) -> None:
    description = input("Nhập mô tả công việc: ").strip()
    due_str = input("Nhập ngày hạn (YYYY-MM-DD): ").strip()

    try:
        due_date = datetime.strptime(due_str, "%Y-%m-%d")
    except ValueError:
        print("Ngày không đúng định dạng YYYY-MM-DD")
        return

    tasks.append(Task(description, due_date))
    print("Đã thêm task mới.")


def mark_task_done(tasks: list[Task]) -> None:
    if not tasks:
        print("Không có task nào.")
        return

    for i, task in enumerate(tasks, start=1):
        if task.status != "done":
            print(f"{i}. {task}")

    try:
        choice = int(input("Nhập số thứ tự task cần đánh dấu DONE: "))
        if choice < 1 or choice > len(tasks) or tasks[choice - 1].status == "done":
            raise ValueError("Chọn task không hợp lệ!")
        tasks[choice - 1].status = "done"
        print("Đã đánh dấu task là DONE.")
    except ValueError:
        print("Số thứ tự không hợp lệ.")
