n = int(input())

numbers_stack = []

for _ in range(n):
    query = input().split()
    if len(query) > 1:
        numbers_stack.append(int(query[1]))
    else:
        if numbers_stack:
            q_type = query[0]
            if q_type == '2':
                numbers_stack.pop()
            elif q_type == '3':
                print(max(numbers_stack))
            else:
                print(min(numbers_stack))

result = []
while numbers_stack:
    result.append(str(numbers_stack.pop()))

print(', '.join(result))
