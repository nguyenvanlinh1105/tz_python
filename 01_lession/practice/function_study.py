print("BTTH 6.4")

def input_positive_number(prompt: str) -> int:
    value = input(prompt)
    while not (value.isdigit() and int(value) > 0):
        print("Vui lòng nhập số nguyên dương (> 0)!")
        value = input(prompt)
    return int(value)

print("\nBTTH 7.a")
def sum_to_n(number: int) -> int:
    s = 0
    for i in range(1, number + 1):
        s += i
    return s

n = input_positive_number("Nhập n: ")
print(f"Tổng từ 1 đến {n} = {sum_to_n(n)}")


print("\nBTTH 7.b")
def is_leap_year(year: int) -> bool:
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

year = input_positive_number("Nhập năm: ")

if is_leap_year(year):
    print(f"{year} là năm nhuận")
else:
    print(f"{year} không phải năm nhuận")


print("\n BTTH 7.c")
def count_char(string: str, char: str) -> int:
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

string = input("Nhập chuỗi: ")

char = input(f'Nhập ký tự cần đếm trong chuỗi "{string}": ')
while len(char) != 1:
    print("Vui lòng chỉ nhập 1 ký tự!")
    char = input(f'Nhập ký tự cần đếm trong chuỗi "{string}": ')

print(f'Số lần xuất hiện của "{char}" trong "{string}" là: {count_char(string, char)}')

print("\nBTTH 8")
def format_name(first: str, last: str, middle: str | None = None) -> str:
    if middle is None:
        return f"{first} {last}"
    return f"{first} {middle} {last}"

print(format_name("Linh", "Nguyen"))
print(format_name("Linh", "Nguyen", "Van"))