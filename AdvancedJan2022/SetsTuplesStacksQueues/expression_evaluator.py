from collections import deque

expression = input().split()

numbers = deque()
operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
}

for ch in expression:
    if ch in '+-*/':
        while len(numbers) > 1:
            first = numbers.popleft()
            second = numbers.popleft()
            result = operations[ch](first, second)
            numbers.appendleft(result)

    else:
        numbers.append(int(ch))

print(numbers[0])

