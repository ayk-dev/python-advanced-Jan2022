from collections import deque

chocolates_stack = [int(x) for x in input().split(', ')]
cups_of_milk = deque([int(x) for x in input().split(', ')])

milkshakes = 0
while chocolates_stack and cups_of_milk:
    chocolate = chocolates_stack.pop()
    milk = cups_of_milk.popleft()

    if chocolate <= 0 and milk <= 0:
        continue

    if chocolate <= 0:
        cups_of_milk.appendleft(milk)
        continue

    if milk <= 0:
        chocolates_stack.append(chocolate)
        continue

    if chocolate == milk:
        milkshakes += 1
        if milkshakes == 5:
            break
    else:
        cups_of_milk.append(milk)
        chocolate -= 5
        chocolates_stack.append(chocolate)


if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

chocolates = ''
milks = ''
if chocolates_stack:
    chocolates = ", ".join([str(x) for x in chocolates_stack])
else:
    chocolates = 'empty'
print(f'Chocolate: {chocolates}')
if cups_of_milk:
    milks = ", ".join([str(x) for x in cups_of_milk])
else:
    milks = 'empty'
print(f'Milk: {milks}')