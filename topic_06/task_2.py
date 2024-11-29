# Невідсортований список словників
students = [
    {"ім'я": "Богдан", "оцінка": 85},
    {"ім'я": "Анжела", "оцінка": 92},
    {"ім'я": "Іван", "оцінка": 78},
    {"ім'я": "Назар", "оцінка": 88}
]

# Сортування за ім'ям
sorted_by_name = sorted(students, key=lambda student: student["ім'я"])
print("Список, відсортований за ім'ям:")
print(sorted_by_name)

# Сортування за оцінкою
sorted_by_grade = sorted(students, key=lambda student: student["оцінка"])
print("\nСписок, відсортований за оцінкою:")
print(sorted_by_grade)
