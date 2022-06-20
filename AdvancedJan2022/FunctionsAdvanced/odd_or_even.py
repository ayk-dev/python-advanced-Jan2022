def sum_of_odd_numbers(*args):
    odd_numbers = list(filter(lambda x: x % 2 == 1, *args))
    return sum(odd_numbers) * len(*args)


def sum_of_even_numbers(*args):
    even_numbers = list(filter(lambda x: x % 2 == 0, *args))
    return sum(even_numbers) * len(*args)


command = input()

numbers = [int(x) for x in input().split()]

operations = {
    'Odd': sum_of_odd_numbers,
    'Even': sum_of_even_numbers
}

print(operations[command](numbers))