n, m = input().split()

set_one = set()
set_two = set()

for _ in range(int(n)):
    set_one.add(int(input()))

for _ in range(int(m)):
    set_two.add(int(input()))

result = set_one.intersection(set_two)

for el in result:
    print(el)