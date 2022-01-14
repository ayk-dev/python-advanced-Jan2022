expression = input()

is_balanced = True
brackets_stack = []

if len(expression) % 2 != 0:
    is_balanced = False
else:
    for ch in expression:
        if ch in '{([':
            brackets_stack.append(ch)
        else:
            pair = brackets_stack.pop() + ch
            if pair not in '{}[]()':
                is_balanced = False
                break

if is_balanced:
    print('YES')
else:
    print('NO')