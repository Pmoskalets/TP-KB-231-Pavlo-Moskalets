def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: введено неправильне число. Спробуйте ще раз.")

def get_operation():
    while True:
        operation = input("Виберіть операцію (+, -, *, /): ")
        if operation in ('+', '-', '*', '/'):
            return operation
        else:
            print("Помилка: операція не підтримується. Спробуйте ще раз.")

def calculate(num1, num2, operation):
    try:
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            return num1 / num2
    except ZeroDivisionError:
        print("Помилка: ділення на нуль.")
        return None

def main():
    print("Програма калькулятор")
    while True:
        num1 = get_number("Введіть перше число: ")
        num2 = get_number("Введіть друге число: ")
        operation = get_operation()
        
        result = calculate(num1, num2, operation)
        
        if result is not None:
            print(f"Результат: {num1} {operation} {num2} = {result}")
        
        again = input("Бажаєте продовжити? (y/n): ").lower()
        if again != 'y':
            print("Дякую за використання калькулятора. До побачення!")
            break

main()
