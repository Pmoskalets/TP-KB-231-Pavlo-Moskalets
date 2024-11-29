class Student:
    def __init__(self, name, age):
        """Ініціалізує об'єкт студента з ім'ям та віком."""
        self.name = name
        self.age = age

    def __repr__(self):
        """Забезпечує зручне текстове представлення об'єкта."""
        return f"Student(name='{self.name}', age={self.age})"


# Створення списку студентів
students = [
    Student("Сергій", 19),
    Student("Олена", 22),
    Student("Іван", 20),
    Student("Тетяна", 18),
    Student("Богдан", 21),
]

# Сортування списку студентів за віком (ключ - атрибут age)
sorted_by_age = sorted(students, key=lambda student: student.age)

# Виведення списку у відсортованому порядку
print("Сортування за віком:")
for student in sorted_by_age:
    print(student)

# Сортування списку студентів за ім'ям (ключ - атрибут name)
sorted_by_name = sorted(students, key=lambda student: student.name)

print("\nСортування за ім'ям:")
for student in sorted_by_name:
    print(student)
