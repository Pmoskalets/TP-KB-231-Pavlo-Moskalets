# calc.py

from operations import perform_operation

def main():
    print("Калькулятор")
    print("Доступні операції: додавання, віднімання, множення, ділення")

    while True:
        operation = input("Введіть операцію (або 'вихід' для завершення): ").lower()
        if operation == "вихід":
            print("Дякую за використання калькулятора!")
            break
        result = perform_operation(operation)
        print(f"Результат: {result}")

if __name__ == "__main__":
    main()
