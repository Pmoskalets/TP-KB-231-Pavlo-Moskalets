def infix_to_rpn(expression):
    """
    Перетворює інфіксний вираз у зворотний польський запис (ЗПН).
    """
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    operators = []

    def is_operator(c):
        return c in precedence

    def greater_precedence(op1, op2):
        return precedence[op1] > precedence[op2] or (precedence[op1] == precedence[op2] and op1 != '^')

    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
    for token in tokens:
        if token.isdigit() or token.replace('.', '', 1).isdigit():
            output.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()  # Видаляємо '('
        elif is_operator(token):
            while operators and operators[-1] != '(' and greater_precedence(operators[-1], token):
                output.append(operators.pop())
            operators.append(token)

    while operators:
        output.append(operators.pop())

    return output


def evaluate_rpn(rpn):
    """
    Обчислює результат виразу у зворотному польському записі (ЗПН).
    """
    stack = []

    for token in rpn:
        if token.isdigit() or token.replace('.', '', 1).isdigit():
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '^':
                stack.append(a ** b)

    return stack[0]


def main():
    print("Введіть математичний вираз з операторами (+, -, *, /, ^) та дужками:")
    expression = input().strip()
    
    # Етап 1: Перетворення в ЗПН
    rpn = infix_to_rpn(expression)
    print("Зворотний польський запис (ЗПН):", " ".join(rpn))
    
    # Етап 2: Обчислення ЗПН
    result = evaluate_rpn(rpn)
    print("Результат:", result)


if __name__ == "__main__":
    main()
