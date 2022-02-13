rows, cols = [int(x) for x in input().split(' ')]
snake = input()

idx = 0

for row in range(rows):
    row_elements = [None] * cols
    if row % 2 == 0:
        for col in range(cols):
            row_elements[col] = snake[idx % len(snake)]
            idx += 1
    else:
        for col in range(cols - 1, -1, -1):
            row_elements[col] = snake[idx % len(snake)]
            idx += 1
    print(*row_elements, sep='')
