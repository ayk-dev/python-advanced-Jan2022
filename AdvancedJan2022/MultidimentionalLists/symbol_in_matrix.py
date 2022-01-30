n = int(input())

matrix = [list(input()) for _ in range(n)]

symbol = input()
is_found = False

for i in range(n):
    if symbol in matrix[i]:
        print(f'({i}, {matrix[i].index(symbol)})')
        is_found = True
        break

if not is_found:
    print(f'{symbol} does not occur in the matrix')


