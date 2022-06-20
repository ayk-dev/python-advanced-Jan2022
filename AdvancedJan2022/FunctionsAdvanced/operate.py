from functools import reduce


def operate(operator, *args):
    result = None
    if operator == '+':
        result = reduce(lambda a, b: a + b, args, 0)
    elif operator == '-':
        result = reduce(lambda a, b: a - b, args)
    elif operator == '*':
        result = reduce(lambda a, b: a * b, args, 1)
    elif operator == '/':
        result = reduce(lambda a, b: a / b, args)

    return result


print(operate("/", 1, 2, 3))
print(operate("*", 3, 4))



