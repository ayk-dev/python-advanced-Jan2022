n = int(input())

matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split(' ')])

sum_primary_diag = 0
for i in range(n):
    sum_primary_diag += matrix[i][i]

print(sum_primary_diag)