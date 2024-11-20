# functions.py

def add(a, b):
    """Функція для додавання двох чисел"""
    return a + b

def subtract(a, b):
    """Функція для віднімання двох чисел"""
    return a - b

def multiply(a, b):
    """Функція для множення двох чисел"""
    return a * b

def divide(a, b):
    """Функція для ділення двох чисел"""
    if b == 0:
        raise ValueError("Ділення на нуль неможливе!")
    return a / b
