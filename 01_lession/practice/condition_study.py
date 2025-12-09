print("CHƯƠNG TRÌNH KIỂM TRA TUỔI HEHE :))")
print("------------------")
print("BTTH 1")
def confirmAge (age:int) -> str:
    if(age < 0):
        return "Lớn rồi mà nhập tuổi âm hehe"
    if (age <= 11):
        return "Trẻ con"
    elif (age <= 17):
        return "Thiếu niên"
    elif (age <= 30):
        return "Thanh niên"
    else:
        return "Người già"

print("Nhập tuổi để kiểm tra: \n")
a = int(input())

print(confirmAge(a))

print("BTTH 2")
n = int(input("Nhập số nguyên dương: "))
if n < 0:
    print("Vui lòng nhập số nguyên dương")
else:
    result = "Even" if n % 2 == 0 else "Odd"
    print(result)

print("BTTH 3")
year = int(input("Nhập năm: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} là năm nhuận")
else:
    print(f"{year} không phải năm nhuận")







