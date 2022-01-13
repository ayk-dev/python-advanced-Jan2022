numbers_stack = [int(n) for n in input().split()]

while numbers_stack:
    print(numbers_stack.pop(), end=' ')

