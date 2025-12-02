def decimal_to_binary(decimal_num):
    """
    Функция переводит десятичное число в двоичное
    """
    if decimal_num == 0:
        return "0"

    binary_str = ""
    num = decimal_num

    while num > 0:
        binary_str = str(num % 2) + binary_str
        num = num // 2

    return binary_str


# Основная программа
decimal_num = int(input("Введите десятичное число: "))
binary_num = decimal_to_binary(decimal_num)
print(f"Десятичное число: {decimal_num}")
print(f"Двоичное представление: {binary_num}")