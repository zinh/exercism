import re

def calculate(question):
    numbers = re.findall(r'(-?[0-9]+)', question)
    operators = re.findall(r'(plus|minus|multiplied|divided)', question)
    expr = []
    if len(numbers) == 0:
        raise ValueError("Invalid question")
    for idx, number in enumerate(numbers):
        expr.append(int(number))
        if idx < len(operators):
            expr.append(operators[idx])
    if len(expr) <= 1:
        raise ValueError("Invalid question")
    return evaluate(expr)

def evaluate(expr):
    stack = [expr[0]]
    for el in expr[1:]:
        if type(el) is int and type(stack[-1]) is not int:
            result = calc(stack.pop(), stack.pop(), el)
            stack.append(result)
        else:
            stack.append(el)
    if len(stack) > 1:
        raise ValueError('Invalid expression')
    return stack[0]

def calc(op, e1, e2):
    if op == 'plus':
        return e1 + e2
    elif op == 'minus':
        return e1 - e2
    elif op == 'multiplied':
        return e1 * e2
    elif op == 'divided':
        return e1 / e2
