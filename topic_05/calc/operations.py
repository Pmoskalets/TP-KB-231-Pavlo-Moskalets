# operations.py

from functions import add, subtract, multiply, divide

def get_numbers():
    """Функція для отримання двох чисел від користувача"""
    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        return a, b
    except ValueError:
        raise ValueError("Будь ласка, введіть числові значення!")

def perform_operation(operation):
    """Функція для виконання вибраної операції"""
    try:
        a, b = get_numbers()
        if operation == "додавання":
            return add(a, b)
        elif operation == "віднімання":
            return subtract(a, b)
        elif operation == "множення":
            return multiply(a, b)
        elif operation == "ділення":
            return divide(a, b)
        else:
            raise ValueError("Невідома операція!")
    except Exception as e:
        return f"Помилка: {e}"
