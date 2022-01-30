rows = int(input())

flat_matrix = []

for _ in range(rows):
    matrix_row = [int(x) for x in input().split(', ')]
    flat_matrix.extend(matrix_row)

print(flat_matrix)