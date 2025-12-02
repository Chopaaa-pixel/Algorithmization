# Ввод данных
num = int(input("Введите натуральное число: "))

# Инициализация переменных
max_digit = 0

# Объявление цикла while
while num > 0:
    # Тело цикла - извлечение цифры и сравнение
    digit = num % 10
    if digit > max_digit:
        max_digit = digit
    num = num // 10

# Вывод результата
print("Наибольшая цифра в числе:", max_digit)