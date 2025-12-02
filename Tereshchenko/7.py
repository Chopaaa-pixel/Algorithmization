# Открытие файла для записи
filename = "номер_группы.txt"

with open(filename, 'w', encoding='utf-8') as file:
    print("Введите данные студентов (для завершения введите 'стоп' в поле фамилии)")

    while True:
        # Ввод данных
        surname = input("Введите фамилию студента: ")

        # Проверка условия завершения
        if surname.lower() == 'стоп':
            break

        email = input("Введите номер группы: ")

        # Запись данных в файл
        file.write(f"{surname} {email}\n")
        print("Данные записаны.")

print("\nЧтение данных из файла:")
print("=" * 30)

# Открытие файла для чтения
with open(filename, 'r', encoding='utf-8') as file:
    # Чтение и вывод всех строк
    for line in file:
        print(line.strip())