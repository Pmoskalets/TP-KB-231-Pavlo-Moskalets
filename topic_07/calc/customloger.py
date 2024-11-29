import logging

class OperationLogger:
    def __init__(self, log_file="math_operations.log"):
        self.logger = logging.getLogger("OperationLogger")
        self.logger.setLevel(logging.INFO)

        # Створюємо об'єкт для запису у файл
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))

        # Додаємо обробник до логгера
        if not self.logger.hasHandlers():
            self.logger.addHandler(file_handler)

    def log_operation(self, operand1, operand2, operator, outcome):
        self.logger.info(
            f"Operand 1: {operand1}, Operand 2: {operand2}, Operator: {operator}, Result: {outcome}"
        )
