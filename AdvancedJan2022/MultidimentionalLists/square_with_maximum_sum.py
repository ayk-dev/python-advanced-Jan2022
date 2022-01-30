rows, cols = [int(x) for x in input().split(', ')]

matrix = []
for _ in range(rows):
    matrix.append([int(n) for n in input().split(', ')])

submatrixes = []
max_sum = 0
max_submatrix = []
for i in range(rows - 1):
    for j in range(cols - 1):
        submatrix = [matrix[i][j], matrix[i][j + 1],
                     matrix[i + 1][j],matrix[i + 1][j + 1]]
        sum_submatrix = sum(submatrix)
        if sum_submatrix > max_sum:
            max_sum = sum_submatrix
            max_submatrix = submatrix.copy()

print(max_submatrix[0], max_submatrix[1])
print(max_submatrix[2], max_submatrix[3])
print(max_sum)

