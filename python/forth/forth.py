from functools import reduce
import re

class StackUnderflowError(Exception):
    pass

class Stack:
    def __init__(self):
        self.stack = []

    def __repr__(self):
        return str(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack == []:
            raise StackUnderflowError("Stack underflow")
        item = self.stack[-1]
        self.stack = self.stack[0:-1]
        return item

    def peek(self):
        if self.stack == []:
            raise StackUnderflowError("Stack underflow")
        return self.stack[-1]

def evaluate(input_data):
    stack = Stack()
    runtime = {}
    statements = reduce(lambda memo, line: memo + parse(line.lower()), input_data, [])
    for stmt in statements:
        stack, runtime = evaluate_token(stmt, stack, runtime)
    return stack.stack


def evaluate_token(token, stack, runtime):
    if token['type'] == 'VAR' or runtime.get(token.get('value')):
        values = runtime.get(token['value'])
        if values == None:
            raise ValueError('Unknown variable name')
        for value in values:
            evaluate_token(value, stack, runtime)
    elif token['type'] == 'INT':
        stack.push(token['value'])
    elif token['type'] == 'IDEF':
        if token['value'] == 'dup':
            stack.push(stack.peek())
        elif token['value'] == 'drop':
            stack.pop()
        elif token['value'] == 'swap':
            a = stack.pop()
            b = stack.pop()
            stack.push(a)
            stack.push(b)
        elif token['value'] == 'over':
            a = stack.pop()
            b = stack.pop()
            stack.push(b)
            stack.push(a)
            stack.push(b)
    elif token['type'] == 'OP':
        b = stack.pop()
        a = stack.pop()
        if token['value'] == '+':
            stack.push(a + b)
        elif token['value'] == '-':
            stack.push(a - b)
        elif token['value'] == '*':
            stack.push(a * b)
        elif token['value'] == '/':
            stack.push(a // b)
    elif token['type'] == 'ASSIGNMENT':
        runtime[token['name']] = reduce_assignment(token['values'], runtime)
    return (stack, runtime)

def parse(line):
    number = re.compile("\d+")
    tokens = line.split(' ')
    # assignment
    if tokens[0] == ':' and tokens[-1] == ';':
        var_name = tokens[1]
        if number.fullmatch(var_name):
            raise ValueError("Invalid indentifer")
        values = tokens[2:-1]
        return [{'type': 'ASSIGNMENT', 'name': var_name, 'values': parse(' '.join(values))}]
    values = []
    for token in tokens:
        if token == 'dup' or token == 'swap' or token == 'drop' or token == 'over' :
            values.append({'type': 'IDEF', 'value': token})
        elif token == '+' or token == '-' or token == '*' or token == '/':
            values.append({'type': 'OP', 'value': token})
        elif number.fullmatch(token):
            values.append({'type': 'INT', 'value': int(token)})
        else:
            values.append({'type': 'VAR', 'value': token})
    return values

def reduce_assignment(tokens, runtime):
    results = []
    for token in tokens:
        if token['type'] == 'VAR':
            token_values = runtime.get(token['value'])
            if token_values == None:
                raise ValueError("Undefined variable")
            else:
                results += token_values
        else:
            results.append(token)
    return results
