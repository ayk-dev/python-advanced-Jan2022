from collections import deque


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_neighbours(row, col, matrix):
    size = len(matrix)
    neighbours = []
    # row, col -1
    if is_inside(row, col - 1, size):
        neighbours.append([row, col -1])
    # row - 1, col -1
    if is_inside(row - 1, col - 1, size):
        neighbours.append([row - 1, col - 1])
    # row - 1, col
    if is_inside(row - 1, col, size):
        neighbours.append([row - 1, col])
    # row - 1, col + 1
    if is_inside(row - 1, col + 1, size):
        neighbours.append([row - 1, col + 1])
    # row, col + 1
    if is_inside(row, col + 1, size):
        neighbours.append([row, col + 1])
    # row + 1, col - 1
    if is_inside(row + 1, col - 1, size):
        neighbours.append([row + 1, col - 1])
    # row + 1, col
    if is_inside(row + 1, col, size):
        neighbours.append([row + 1, col])
    # row + 1, col + 1
    if is_inside(row + 1, col + 1, size):
        neighbours.append([row + 1, col + 1])

    return neighbours


n = int(input())

matrix = [ ]
for _ in range(n):
    matrix.append([int(x) for x in input().split()])

bombs = deque(input().split())

while bombs:
    row, col = [int(x) for x in bombs.popleft().split(',')]
    bomb = matrix[row][col]
    if bomb > 0:
        bomb_neighbours = get_neighbours(row, col, matrix)
        for i in range(len(bomb_neighbours)):
            r = bomb_neighbours[i][0]
            c = bomb_neighbours[i][1]
            if matrix[r][c] > 0:
                matrix[r][c] -= bomb
        matrix[row][col] = 0

alive_cells_count = 0
alive_cells_sum = 0
for i in range(n):
   for cell in matrix[i]:
        if cell > 0:
            alive_cells_count += 1
            alive_cells_sum += cell

print(f'Alive cells: {alive_cells_count}')
print(f'Sum: {alive_cells_sum}')
for row in matrix:
    print(*row, sep=' ')



