from utils.file_utils import read_file_content, count_word_frequency


def count_words_in_file(filename: str) -> None:
    try:
        content = read_file_content(filename)

        freq = count_word_frequency(content)
        total_words = sum(freq.values())

        top_10 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10]

        print(f"\nTổng số từ: {total_words}")
        print("Top 10 từ xuất hiện nhiều nhất:")
        for word, c in top_10:
            print(f"- {word}: {c}")

    except FileNotFoundError:
        print("File không tồn tại")

    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")


def main():
    while True:
        filename = input("\nNhập tên file cần phân tích (hoặc nhập 'exit' để thoát): ")

        if filename.lower() == "exit":
            print("Kết thúc chương trình.")
            break

        count_words_in_file(filename)


if __name__ == "__main__":
    main()
