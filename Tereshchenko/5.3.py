import math
def rectangle_area(length, width):
    """Функция вычисляет площадь прямоугольника"""
    return length * width
def circle_area(radius):
    """Функция вычисляет площадь круга"""
    return math.pi * radius ** 2
def triangle_area(base, height):
    """Функция вычисляет площадь треугольника"""
    return 0.5 * base * height
# Основная программа
print("Выберите фигуру для расчета площади:")
print("1 - Прямоугольник")
print("2 - Круг")
print("3 - Треугольник")
choice = input("Введите номер фигуры (1-3): ")
if choice == "1":
    a = float(input("Введите длину прямоугольника: "))
    b = float(input("Введите ширину прямоугольника: "))
    area = rectangle_area(a, b)
    print(f"Площадь прямоугольника: {area}")
elif choice == "2":
    r = float(input("Введите радиус круга: "))
    area = circle_area(r)
    print(f"Площадь круга: {area:.2f}")
elif choice == "3":
    base = float(input("Введите основание треугольника: "))
    height = float(input("Введите высоту треугольника: "))
    area = triangle_area(base, height)
    print(f"Площадь треугольника: {area}")
else:
    print("Ошибка выбора")