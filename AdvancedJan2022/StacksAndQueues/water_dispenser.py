from collections import deque

quantity = int(input())

people = deque()
name = input()
while not name == 'Start':
    people.append(name)
    name = input()

command = input()
while not command == 'End':
    if 'refill' in command.split():
        litres = int(command.split()[1])
        quantity += litres
    else:
        litres = int(command)
        person_name = people.popleft()
        if litres <= quantity:
            print(f'{person_name} got water')
            quantity -= litres
        else:
            print(f'{person_name} must wait')
    command = input()

print(f'{quantity} liters left')



