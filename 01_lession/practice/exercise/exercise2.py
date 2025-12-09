# Bài tập 2:
# Đề bài: Viết chương trình tính S = 1 + 1/3! + 1/5! + ... + 1/(2n−1)!, với n được nhập từ bàn phím
print("===== BTVN 2: CHƯƠNG TRÌNH TÍNH TỔNG S = 1 + 1/3! + 1/5! + ... + 1/(2n−1)! =====")

def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def calculate_odd_factorial_series(n: int) -> float:
    total = 0
    for i in range(1, n + 1):
        total += 1 / factorial(2 * i - 1)
    return float(total)

print(f"Tổng = {calculate_odd_factorial_series(5)}")

