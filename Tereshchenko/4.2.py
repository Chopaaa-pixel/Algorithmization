# Ввод данных
n = int(input("Введите число n: "))

# Инициализация переменных
total_sum = 0
factorial = 1

# Цикл перебора последовательности
for i in range(1, n + 1):
    # Вычисление факториала текущего числа
    factorial = factorial * i
    # Накопление суммы
    total_sum = total_sum + factorial

# Вывод результата
print("Сумма факториалов 1! + 2! + ... + n! =", total_sum)