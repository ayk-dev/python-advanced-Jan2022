from collections import deque

customers = deque()
name = input()
while not name == 'End':
    if name == 'Paid':
        while customers:
            print(customers.popleft())
    else:
        customers.append(name)

    name = input()

print(f'{len(customers)} people remaining.')

