import logging
from operations import fetch_numbers, execute_operation # type: ignore

# Налаштування логування
logging.basicConfig(
    filename="calc_operations.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def display_menu():
    print("\nДоступні операції:")
    operations = [
        "1. Додавання (+)",
        "2. Віднімання (-)",
        "3. Множення (*)",
        "4. Ділення (/)",
        "5. Остача (%)",
        "6. Піднесення до степеня (**)",
        "7. Цілочисельне ділення (//)",
    ]
    for op in operations:
        print(op)

def process_choice(choice):
    operation_map = {
        '1': '+', '2': '-', '3': '*', '4': '/', 
        '5': '%', '6': '**', '7': '//'
    }
    return operation_map.get(choice, None)

def run_calculator():
    print("Ласкаво просимо до калькулятора!")
    print("Введіть 'вихід', щоб завершити роботу.")

    while True:
        display_menu()
        user_input = input("Оберіть операцію (1-7) або 'вихід': ").strip().lower()

        if user_input == 'вихід':
            logging.info("Користувач завершив сесію.")
            print("До побачення!")
            break

        operation = process_choice(user_input)
        if not operation:
            print("Некоректний вибір. Спробуйте ще раз.")
            continue

        # Отримання чисел від користувача
        try:
            num1, num2 = fetch_numbers()
        except ValueError:
            print("Помилка вводу! Введіть два числа.")
            logging.warning("Невірний формат вводу чисел.")
            continue

        # Виконання операції
        try:
            result = execute_operation(operation, num1, num2)
            print(f"Результат: {result}")
            logging.info(f"Операція {operation} виконана з результатом {result}.")
        except Exception as e:
            print(f"Сталася помилка: {e}")
            logging.error(f"Помилка під час операції: {e}")

# Запуск калькулятора
if __name__ == "__main__":
    logging.info("Старт програми 'Калькулятор'.")
    try:
        run_calculator()
    finally:
        logging.info("Програма завершена.")
