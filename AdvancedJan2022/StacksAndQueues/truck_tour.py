from collections import deque

n = int(input()) # number of petrol pumps

pumps = deque()
for _ in range(n):
    pump = [int(x) for x in input().split()]
    pumps.append(pump)

for index in range(n):
    tank = 0

    is_valid = False
    for fuel, distance in pumps:
        tank += fuel
        if tank >= distance:
            is_valid = True
            tank -= distance
        else:
            is_valid = False
            # pumps.append(pumps.popleft()) this line equals the line below
            pumps.rotate(-1)
            break

    if is_valid:
        print(index)
        break




