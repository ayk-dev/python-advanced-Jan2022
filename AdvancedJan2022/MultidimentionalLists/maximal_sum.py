rows, cols = [int(n) for n in input().split()]

matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

max_sum = -999999999999999
max_square = []

for i in range(rows - 2):
    for j in range(cols - 2):
        square = [
            matrix[i][j], matrix[i][j + 1], matrix[i][j + 2],
            matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2],
            matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]
        ]
        square_sum = sum(square)
        if square_sum > max_sum:
            max_sum = square_sum
            max_square = square

print(f'Sum = {max_sum}')
print(max_square[0], max_square[1], max_square[2])
print(max_square[3], max_square[4], max_square[5])
print(max_square[6], max_square[7], max_square[8])
