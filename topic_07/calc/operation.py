import logging
from functions import add, subtract, multiply, divide, modulus, exponent, floor_division # type: ignore


class CalculatorEngine:
    def __init__(self):
        self.operations = {
            '1': ('Addition', add),
            '+': ('Addition', add),
            '2': ('Subtraction', subtract),
            '-': ('Subtraction', subtract),
            '3': ('Multiplication', multiply),
            '*': ('Multiplication', multiply),
            '4': ('Division', divide),
            '/': ('Division', divide),
            '5': ('Modulus', modulus),
            '%': ('Modulus', modulus),
            '6': ('Exponentiation', exponent),
            '**': ('Exponentiation', exponent),
            '7': ('Floor Division', floor_division),
            '//': ('Floor Division', floor_division),
        }

    def input_numbers(self):
        try:
            first = float(input("Enter first number: "))
            second = float(input("Enter second number: "))
            return first, second
        except ValueError as e:
            logging.warning(f"Invalid input by user: {e}")
            print("Please enter valid numeric values!")
            return None, None

    def execute_operation(self, user_choice):
        if user_choice not in self.operations:
            logging.warning(f"Invalid operation selected: {user_choice}")
            print("Operation not recognized. Try again!")
            return

        first, second = self.input_numbers()
        if first is None or second is None:
            return

        operation_name, operation_func = self.operations[user_choice]
        try:
            result = operation_func(first, second)
            logging.info(f"Operation: {operation_name}, Inputs: {first}, {second}, Result: {result}")
            print(f"Operation {operation_name}: Result = {result}")
        except Exception as e:
            logging.error(f"Error during operation '{operation_name}': {e}")
            print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    logging.basicConfig(
        filename="calculator_operations.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    calc_engine = CalculatorEngine()

    while True:
        print("\nSelect an operation:")
        print("1 (+) Add")
        print("2 (-) Subtract")
        print("3 (*) Multiply")
        print("4 (/) Divide")
        print("5 (%) Modulus")
        print("6 (**) Exponentiation")
        print("7 (//) Floor Division")
        user_input = input("Your choice (or 'q' to quit): ").strip()

        if user_input.lower() == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        calc_engine.execute_operation(user_input)
