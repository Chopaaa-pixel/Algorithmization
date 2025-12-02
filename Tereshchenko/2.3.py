# Ввод данных
choice = input("Выберите направление (C - из Цельсия в Фаренгейт, F - из Фаренгейта в Цельсий): ")

# Проверка условия и выбор направления
if choice == "C":
    celsius = float(input("Введите температуру в градусах Цельсия: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")
elif choice == "F":
    fahrenheit = float(input("Введите температуру в градусах Фаренгейта: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F = {celsius}°C")
else:
    print("Ошибка: введите C или F")