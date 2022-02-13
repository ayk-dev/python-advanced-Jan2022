rows, cols = [int(n) for n in input().split()]

matrix = [input().split() for _ in range(rows)]

equal_squares = 0

for i in range(rows - 1):
    for j in range(cols - 1):
        square = [matrix[i][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1]]
        if square[0] == square[1] and square[1] == square[2] and square[2] == square[3]:
            equal_squares += 1

print(equal_squares)

