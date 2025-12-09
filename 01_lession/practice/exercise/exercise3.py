# Bài tập 3
# Đề bài: Viết chương trình để chuẩn hoá câu:
#
# Bỏ khoảng trắng thừa (giữa các từ chỉ còn 1 khoảng trắng)
# Viết hoa chữ cái đầu câu
# Đảm bảo câu kết thúc bằng chính xác một dấu chấm “.”
# Nếu thừa nhiều dấu chấm liên tiếp thì rút gọn còn “.”
# Ví dụ: "Hello worlD, this Is python.. " => "Hello world, this is python."

print("===== BTVN 3: CHƯƠNG TRÌNH CHUẨN HOÁ CHUỖI =====")
input_text = input("Nhập chuỗi bất kỳ: ")

def normalize_string(text: str) -> str:
    normalized = text.lower()

    for char in [".", ",", "!", "?"]:
        normalized = normalized.replace(char, "")

    words = normalized.split()
    words[0] = words[0].capitalize()

    result = " ".join(words) + "."
    return result

print(normalize_string(input_text))
