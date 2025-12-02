def calculate_factorial_sum(n):
    """
    Функция вычисляет сумму факториалов 1! + 2! + ... + n!
    """
    total_sum = 0
    factorial = 1

    for i in range(1, n + 1):
        factorial = factorial * i
        total_sum = total_sum + factorial

    return total_sum


# Основная программа
n = int(input("Введите число n: "))
result = calculate_factorial_sum(n)
print("Сумма факториалов:", result)