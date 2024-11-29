class Person:
    def __init__(self, name, age):
        self.name = name  # Ініціалізуємо ім'я
        self.age = age    # Ініціалізуємо вік

# Створення об'єкта
person1 = Person("Alice", 30)

print(person1.name)  # Виведе: Alice
print(person1.age)   # Виведе: 30
