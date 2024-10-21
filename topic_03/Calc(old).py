def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "На нуль ділити не можна!"

def calculator():
    print("Вітаємо у калькуляторі! Для виходу введіть 'exit'.")
    
    while True:
        # Введення першого числа або команди для виходу
        num1 = input("Введіть перше число або 'exit' для завершення програми: ")
        if num1.lower() == 'exit':
            print("Програма завершена.")
            break
        
        # Перевірка, чи введене значення є числом
        try:
            num1 = float(num1)
        except ValueError:
            print("Некоректний ввід. Спробуйте ще раз.")
            continue

        # Введення операції
        operation = input("Виберіть операцію (+, -, *, /): ")
        if operation not in ['+', '-', '*', '/']:
            print("Невірна операція. Спробуйте ще раз.")
            continue
        
        # Введення другого числа або команди для виходу
        num2 = input("Введіть друге число або 'exit' для завершення програми: ")
        if num2.lower() == 'exit':
            print("Програма завершена.")
            break

        # Перевірка, чи введене значення є числом
        try:
            num2 = float(num2)
        except ValueError:
            print("Некоректний ввід. Спробуйте ще раз.")
            continue

        # Виконання обраної операції
        if operation == '+':
            print(f"Результат: {add(num1, num2)}")
        elif operation == '-':
            print(f"Результат: {subtract(num1, num2)}")
        elif operation == '*':
            print(f"Результат: {multiply(num1, num2)}")
        elif operation == '/':
            print(f"Результат: {divide(num1, num2)}")

if __name__ == "__main__":
    calculator()
