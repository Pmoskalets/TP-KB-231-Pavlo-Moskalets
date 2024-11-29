from custom_logger import Logger # type: ignore
from functions import MathOperations # type: ignore
from operations import UserInput # type: ignore


class MathCalculator:
    def __init__(self):
        self.logger = Logger()
        self.math_operations = MathOperations()
        self.user_input = UserInput()

    def record_operation(self, operand1, operand2, operator, outcome):
        self.logger.log_operation(operand1, operand2, operator, outcome)

    def perform_calculations(self):
        current_value = self.user_input.get_number()
        while True:
            next_value = self.user_input.get_number()
            operation = self.user_input.get_operator(current_value)

            if operation == "+":
                outcome = self.math_operations.add(current_value, next_value)
            elif operation == "-":
                outcome = self.math_operations.subtract(current_value, next_value)
            elif operation == "!-":
                outcome = self.math_operations.reverse_subtract(current_value, next_value)
            elif operation == "*":
                outcome = self.math_operations.multiply(current_value, next_value)
            elif operation == "/":
                outcome = self.math_operations.divide(current_value, next_value)
            elif operation == "!/":
                outcome = self.math_operations.reverse_divide(current_value, next_value)
            elif operation == "^":
                outcome = self.math_operations.power(current_value, next_value)
            elif operation == "!^":
                outcome = self.math_operations.reverse_power(current_value, next_value)
            else:
                print("Невідома операція! Спробуйте ще раз.")
                continue

            self.record_operation(current_value, next_value, operation, outcome)
            current_value = outcome
            print("\nРезультат зараз =", current_value)


if __name__ == "__main__":
    calculator = MathCalculator()
    calculator.perform_calculations()
