import logging
from operations import add_numbers, subtract_numbers, multiply_numbers, divide_numbers, calculate_remainder, power_of, floor_divide # type: ignore

def fetch_inputs():
    """Отримує числа від користувача з обробкою помилок."""
    try:
        first = float(input("Input the first number: "))
        second = float(input("Input the second number: "))
        return first, second
    except ValueError:
        logging.warning("User entered invalid data.")
        print("Error! Please enter valid numbers.")
        return None, None

def execute_operation(option, first, second):
    """Виконує операцію відповідно до вибору користувача."""
    result = None
    action_name = ""

    if option in ('1', '+'):
        result = add_numbers(first, second)
        action_name = "Addition"
    elif option in ('2', '-'):
        result = subtract_numbers(first, second)
        action_name = "Subtraction"
    elif option in ('3', '*'):
        result = multiply_numbers(first, second)
        action_name = "Multiplication"
    elif option in ('4', '/'):
        result = divide_numbers(first, second)
        action_name = "Division"
    elif option in ('5', '%'):
        result = calculate_remainder(first, second)
        action_name = "Remainder Calculation"
    elif option in ('6', '**'):
        result = power_of(first, second)
        action_name = "Exponentiation"
    elif option in ('7', '//'):
        result = floor_divide(first, second)
        action_name = "Floor Division"
    else:
        logging.warning("Invalid operation choice by user.")
        print("Invalid operation selected!")
        return None

    if result is not None:
        logging.info(f"Operation: {action_name}, Inputs: {first}, {second}, Result: {result}")
        print(f"Result of {action_name}: {result}")
    return result
