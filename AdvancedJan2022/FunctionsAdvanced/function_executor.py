def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    list_of_results = []
    for func_and_args in args:
        result = func_and_args[0](*func_and_args[1])
        list_of_results.append(result)

    return list_of_results


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))




