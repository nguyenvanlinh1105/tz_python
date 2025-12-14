# try:
#     # đoạn code có nguy cơ lỗi
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Không thể chia cho 0!")
#
# try:
#     raw = input("Nhập một số nguyên: ")
#     x = int(raw)
#     y = 10 / x
#     print(f"Kết quả 10 / {x} =", y)
# except ValueError:
#     print("Lỗi: Bạn phải nhập một số nguyên hợp lệ!")
# except ZeroDivisionError:
#     print("Lỗi: Không thể chia cho 0!")
# except Exception as e:
#     print("Lỗi không xác định:", e)
#
# # Đóng kết nối DB
# try:
#     conn = connect_to_db() # mở kết nối DB
#     result = conn.query("SELECT * FROM users")
#     print(result)
# except Exception as e:
#     print("Lỗi khi truy vấn:", e)
# finally:
#     print("Đóng kết nối DB…")
#     conn.close()
#
# # Reset trạng thái hệ thống
# state = "busy"
#
# try:
#     print("Đang chạy tác vụ quan trọng…")
#     # risky_task()
# except Exception:
#     print("Tác vụ lỗi!")
# finally:
#     state = "idle"
#     print("Trạng thái đã reset về:", state)

# def divide(a, b):
#     if b == 0:
#         raise ValueError("b không được = 0")
#     return a / b
#
# try:
#     divide(5, 0)
# except ValueError as e:
#     print("Lỗi:", e)
#
#
#

#
#
#
# # BTTH1:
# while True:
#    try:
#         a = int(input())
#    except ValueError as e:
#         print("a phải là số")
#         continue
#    print(a)
#
# # BTTH2:
# while True:
#     print("\n=== MENU ===")
#     print("1. Xin chào")
#     print("2. Tính chỉ số BMI")
#     print("3. Thoát")
#
#     try:
#         choice = int(input("Mời bạn chọn (1-3): "))
#     except ValueError:
#         print("Lỗi: Giá trị nhập phải là số!")
#         continue
#
#     if choice not in [1, 2, 3]:
#         print("Lỗi: Giá trị phải nằm trong khoảng 1 đến 3!")
#         continue
#
#     if choice == 1:
#         print("Xin chào bạn ")
#
#     elif choice == 2:
#         try:
#             can_nang = float(input("Nhập cân nặng (kg): "))
#             chieu_cao = float(input("Nhập chiều cao (m): "))
#             bmi = can_nang / (chieu_cao ** 2)
#             print(f" Chỉ số BMI của bạn là: {bmi:.2f}")
#         except ValueError:
#             print("Cân nặng và chiều cao phải là số!")
#
#     elif choice == 3:
#         print(" Thoát chương trình. Tạm biệt!")
#         break


# --- Xử lý chức năng ---
import time

start = time.time()

# --- đoạn code cần đo thời gian ---
result = 0
for i in range(1_000_000):
    result += i
# ----------------------------------

end = time.time()
elapsed = end - start
print("Thời gian thực thi:", elapsed, "giây")


def introduce(
    name: str, age: int, *skills, title: str = "N/A", level: str = "basic", **extra_info
) -> None:
    print("Name:", name)
    print("Age:", age)
    print("Skills:", skills)
    print("Title:", title)
    print("Level:", level)
    print("Extra:", extra_info)


introduce(
    "An",
    20,
    "Python",
    "Java",
    title="Developer",
    level="Fresher",
    hobby="gaming",
    city="Danang",
)
