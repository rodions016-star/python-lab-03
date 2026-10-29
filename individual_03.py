import sys


if __name__ == "__main__":
    word = input("Введите слово: ")
    s = int(input("Введите номер s: "))
    k = int(input("Введите номер k: "))

    if not 1 <= s < k <= len(word):
        print("Ошибка: требуется 1 <= s < k <= длина слова", file=sys.stderr)
        sys.exit(1)

    # s-я буква имеет индекс s - 1, буквы с (s+1)-й по k-ю — срез word[s:k]
    result = word[:s - 1] + word[s:k] + word[s - 1] + word[k:]
    print(f"Результат: {result}")
