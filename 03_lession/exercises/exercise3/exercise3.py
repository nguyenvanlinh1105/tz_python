from datetime import datetime
from task_service import (
    load_tasks,
    save_tasks,
    add_task,
    mark_task_done,
)


def main():
    FILENAME = "tasks.txt"
    tasks = load_tasks(FILENAME)
    print("======To-do List======")
    while True:
        print("1. Xem tất cả task")
        print("2. Xem các task quá hạn")
        print("3. Thêm task mới")
        print("4. Đánh dấu task là done")
        print("5. Thoát")

        try:
            choice = int(input("Nhập lựa chọn của bạn: "))
        except ValueError as e:
            print("Vui lòng nhập số!")

        match choice:
            case 1:
                if not tasks:
                    print("Không có task nào")
                else:
                    print("Danh sách task hiện tại: \n")
                    for task in tasks:
                        print(task)
                    print("\n")
            case 2:
                now = datetime.now()
                overdue_tasks = [t for t in tasks if t.is_overdue(now)]

                if not overdue_tasks:
                    print("Không có task quá hạn.")
                else:
                    print("Các task quá hạn là:\n")
                    for task in overdue_tasks:
                        print(task)
                    print("\n")
            case 3:
                print("Bạn muốn thêm bao nhiêu task?")
                try:
                    num = int(input())
                    if num <= 0:
                        print("Số task phải lớn hơn 0!")
                        break
                except ValueError:
                    print("Vui lòng nhập số!")
                    break

                for i in range(1, num + 1):
                    print(f"\nNhập thông tin task thứ {i}")
                    add_task(tasks)

                save_tasks(FILENAME, tasks)
            case 4:
                mark_task_done(tasks)
                save_tasks(FILENAME, tasks)

            case 5:
                print("Thoát chương trình")
                break

            case _:
                print("Lựa chọn không hợp lệ. Vui lòng chọn 1–5.")


if __name__ == "__main__":
    main()
