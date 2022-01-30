rows, cols = [int(x) for x  in input().split(', ')]

sum_of_elements = 0
matrix = []

for i in range(rows):
    matrix.append([int(n) for n in input().split(', ')])
    sum_of_elements += sum(matrix[i])

print(sum_of_elements)
print(matrix)