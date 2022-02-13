rows, cols = [int(x) for x in input().split(' ')]

matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        ch1 = chr(i + 97)
        ch2 = chr(i + j + 97)
        ch3 = chr(i + 97)
        element = ch1 + ch2 + ch3
        row.append(element)
    print(' '.join(row))
    matrix.append(row)




    