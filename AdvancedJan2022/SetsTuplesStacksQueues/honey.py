from collections import deque

bees = deque([int(b) for b in input().split()])
nectars_stack = [int(n) for n in input().split()]

symbols = deque(input().split())

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b if b != 0 else 0,
}
total_honey = 0

while bees and nectars_stack:
    bee = bees[0]
    nectar = nectars_stack.pop()

    if nectar >= bee:
        bees.popleft()
        s = symbols.popleft()
        honey_made = abs(operations[s](bee, nectar))
        total_honey += honey_made

print(f'Total honey made: {total_honey}')
if bees:
    print(f'Bees left: {", ".join(str(b) for b in bees)}')
if nectars_stack:
    print(f'Nectar left: {", ".join(str(n) for n in nectars_stack)}')


