from collections import deque

cups_queue = deque(int(x) for x in input().split())
bottles_stack = [int(x) for x in input().split()]

waisted_water = 0
bottles_over = False


while cups_queue:
    cup = cups_queue.popleft()

    while cup > 0:
        bottle = bottles_stack.pop()
        if bottle >= cup:
            bottle -= cup
            cup = 0
            waisted_water += bottle
        else:
            cup -= bottle
        if not bottles_stack:
            bottles_over = True
            break

    if bottles_over:
        break

if cups_queue:
    print(f'Cups: {" ".join(str(c) for c in cups_queue)}')
else:
    print(f'Bottles: {" ".join(str(b) for b in bottles_stack)}')
print(f'Wasted litters of water: {waisted_water}')

