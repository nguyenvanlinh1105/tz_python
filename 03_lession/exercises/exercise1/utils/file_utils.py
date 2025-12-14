def read_file_content(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def count_word_frequency(text: str) -> dict[str, int]:
    text = text.lower()

    punctuation = ".,;:?!()[]"
    for ch in punctuation:
        text = text.replace(ch, "")

    words = text.split()

    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq
