class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def reverse_subtract(x, y):
        return y - x

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            return "Error: Division by zero is undefined. Please choose another number."
        return x / y

    @staticmethod
    def reverse_divide(x, y):
        if x == 0:
            return "Error: Cannot divide by zero. Result is undefined."
        return y / x

    @staticmethod
    def power(base, exponent):
        return base ** exponent

    @staticmethod
    def reverse_power(base, exponent):
        return exponent ** base
