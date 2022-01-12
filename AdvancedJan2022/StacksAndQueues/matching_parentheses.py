# expression = list(input())
#
# indexes = []
# for index in range(len(expression)):
#     if expression[index] == "(":
#         indexes.append(index)
#     elif expression[index] == ')':
#         first_index = indexes.pop()
#         print(''.join(expression[first_index:index + 1]))


# My solution, optimised
expression = list(input())

stacks = []
for el in expression:
    for l in stacks:
        l.append(el)
    if el == '(':
        stacks.append([el])

    elif el == ')':
        result = stacks.pop()
        print("".join(result))



