import random

# Генерация случайного числа
number = random.randint(1, 10)
attempts = 3

print("Угадайте число от 1 до 10. У вас 3 попытки.")

# Цикл с ограниченным количеством итераций
for i in range(attempts):
    # Запрос данных от пользователя
    guess = int(input(f"Попытка {i + 1}. Ваш вариант: "))

    # Проверка условия
    if guess == number:
        print("Поздравляю! Вы угадали!")
        break
    elif guess < number:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")
else:
    # Блок else для цикла (выполняется если не было break)
    print(f"Вы проиграли! Загаданное число: {number}")