rows, cols = [int(x) for x in input().split(', ')]

matrix = []
for _ in range(rows):
    matrix.append([int(n) for n in input().split(' ')])


for j in range(cols):
    sum_of_col = 0
    for i in range(rows):
        sum_of_col += matrix[i][j]
    print(sum_of_col)
