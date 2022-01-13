from collections import deque
import sys


def get_max_element(stack):
    max_element = -sys.maxsize
    while len(stack) > 0:
        elem = stack.pop()
        if elem > max_element:
            max_element = elem
    return max_element


food_quantity = int(input())
orders = [int(o) for o in input().split()]
orders_que = deque()
for order in orders:
    orders_que.append(order)


print(get_max_element(orders))

while orders_que:
    next_customer = int(orders_que.popleft())
    if next_customer <= food_quantity:
        food_quantity -= next_customer
    else:
        orders_que.appendleft(str(next_customer))
        break

if orders_que:
    orders_left = [str(o) for o in orders_que]
    print(f'Orders left: {" ".join(orders_left)}')
else:
    print('Orders complete')


