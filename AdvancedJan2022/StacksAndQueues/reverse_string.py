# Solution 1: not using a stack
# string = input()
# print(string[::-1])


# Solution 2
# text = list(input())
#
# reversed_text = []
#
# for _ in range(len(text)):
#     reversed_text.append(text.pop())
#
# print("".join(reversed_text))


# Solution 3 - simplest
text = list(input())
while text:
    print(text.pop(), end='')



