print("=== THỰC HÀNH CHUỖI ===")

print("\nBTTH 9. Chuẩn hóa họ và tên")
name = "nguyEn VAN LinH"
print(f'Chuẩn hóa "{name}" => {name.title()}')

print("\nBTTH 10. kiểm tra chuỗi đối xứng")
def is_symmetry_chain(s: str) -> bool:
    return s == s[::-1]

print(f'"level" là chuỗi đối xứng? -> {"Yes" if is_symmetry_chain("level") else "No"}')
print(f'"madam" là chuỗi đối xứng? -> {"Yes" if is_symmetry_chain("madam") else "No"}')
print(f'"122 1" là chuỗi đối xứng? -> {"Yes" if is_symmetry_chain("122 1") else "No"}')

print("\nBTTH 11. Đếm số lượng nguyên âm trong chuỗi")
def count_vowels(s: str) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for c in s.lower():
        if c in vowels:
            count += 1
    return count

text = input("Nhập chuỗi bất kì : ")
print(f'Số lượng nguyên âm trong chuỗi {text} là: {count_vowels(text)}')
