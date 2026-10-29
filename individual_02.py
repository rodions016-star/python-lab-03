if __name__ == "__main__":
    text = input("Введите предложение: ")

    result = text.replace("ах", "ух")

    if result:
        print(f"Результат: {result}")
    else:
        print(f"Результат: пустая строка {result!r}")
