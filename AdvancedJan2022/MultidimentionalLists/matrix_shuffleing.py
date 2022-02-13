rows, cols = [int(x) for x in input().split(' ')]

matrix = [input().split() for _ in range(rows)]

cmd = input()
while cmd != 'END':
    cmd_args = cmd.split()
    if cmd_args[0] != 'swap' or len(cmd_args) != 5:
        print('Invalid input!')
        cmd = input()
        continue

    row1, col1 = int(cmd_args[1]), int(cmd_args[2])
    row2, col2 = int(cmd_args[3]), int(cmd_args[4])

    if row1 >= rows or row2 >= rows or col1 >= cols or col2 >= cols:
        print('Invalid input!')
        cmd = input()
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    for i in range(rows):
        print(' '.join(matrix[i]))

    cmd = input()


