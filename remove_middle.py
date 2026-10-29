import sys


if __name__ == "__main__":
    word = input("Введите слово: ")
    if not word:
        print("Ошибка: слово не должно быть пустым", file=sys.stderr)
        sys.exit(1)

    middle = len(word) // 2
    if len(word) % 2 == 1:
        result = word[:middle] + word[middle + 1:]
    else:
        result = word[:middle - 1] + word[middle + 1:]

    print(f"Результат: {result}")
