# operations.py

def add_numbers(num1, num2):
    """Додає два числа."""
    return num1 + num2

def subtract_numbers(num1, num2):
    """Віднімає друге число з першого."""
    return num1 - num2

def multiply_numbers(num1, num2):
    """Множить два числа."""
    return num1 * num2

def divide_numbers(num1, num2):
    """Ділить перше число на друге з перевіркою ділення на нуль."""
    if num2 == 0:
        raise ValueError("Error: Division by zero!")
    return num1 / num2

def calculate_remainder(num1, num2):
    """Знаходить залишок від ділення."""
    return num1 % num2

def power_of(num1, num2):
    """Зводить перше число у ступінь другого."""
    return pow(num1, num2)

def floor_divide(num1, num2):
    """Виконує цілочисельне ділення з перевіркою ділення на нуль."""
    if num2 == 0:
        raise ValueError("Error: Division by zero!")
    return num1 // num2
