def get_diagonal(diag, m):
    result = []
    n = len(m[0])
    if diag == 'primary':
        for i in range(n):
            el = m[i][i]
            result.append(el)

    else:
        for i in range(n):
            el = m[i][n - i - 1]
            result.append(el)
    return result

n = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]

primary = get_diagonal('primary', matrix)
sum_primary_diag = sum(primary)

secondary = get_diagonal('secondary', matrix)
sum_secondary_diag = sum(secondary)

print(f'Primary diagonal: {", ".join(str(el) for el in primary)}. Sum: {sum_primary_diag}')
print(f'Secondary diagonal: {", ".join(str(el) for el in secondary)}. Sum: {sum_secondary_diag}')