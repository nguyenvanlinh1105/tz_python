def say_hello(name: int) -> str:
    print(f"Hello, {name}!")


say_hello("Linh")

print("Nhập n kí tự và đếm tổng số kí tự")

text = input("Nhập 1 chuỗi bất kì")

sum = 0
for chu in text:
    sum += int(chu)

print(f"Tổng số kí tự trong chuỗi {text} là : {sum}")

# BTTH4: Tính tổng từ 1 đến n

print("CHƯƠNG TRÌNH TÍNH TỔNG N SỐ NGUYÊN DƯƠNG")


def sum_n_so(n: int) -> int:
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

# Bài tập 5
while True:
    print("Nhập số nguyên duong n")
    n = int(input())
    if n < 0:
        print("Vui lòng nhập lại số lớn hơn 0")
        break;
    print(f"Tổng {n} là: {sum_n_so(n)} ")

# BTTH 6.1

for i in range(5):
    for j in range(6):
        if(i == 0 or i == 4 or j == 0 or j == 5):
            print("*", end=" ")
        else:
            print("", end=" ")
    print()

# BÀI TẬP 6.2
for i in range(5):
    for j in range(6):
        print("*", end=" ")
    print("")
