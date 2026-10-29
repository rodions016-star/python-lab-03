import sys


if __name__ == "__main__":
    text = input("Введите предложение: ")
    target_length = int(input("Введите требуемую длину: "))

    if text != text.strip(" ") or any(
        char.isspace() and char != " " for char in text
    ):
        print("Ошибка: допустимы только пробелы между словами", file=sys.stderr)
        sys.exit(1)

    words = text.split()
    if len(words) < 2:
        print("Ошибка: требуется не менее двух слов", file=sys.stderr)
        sys.exit(1)

    if not len(text) <= target_length <= 10000:
        print("Ошибка: требуется len(text) <= длина <= 10000", file=sys.stderr)
        sys.exit(1)

    letters_length = 0
    for word in words:
        letters_length += len(word)

    spaces_total = target_length - letters_length
    gaps = len(words) - 1
    base_width = spaces_total // gaps
    extra_gaps = spaces_total % gaps

    parts = []
    for index, word in enumerate(words):
        parts.append(word)
        if index < gaps:
            width = base_width
            if index < extra_gaps:
                width += 1
            parts.append(" " * width)

    result = "".join(parts)
    print(f"Результат: {result}")
    print(f"Длина: {len(result)}")
