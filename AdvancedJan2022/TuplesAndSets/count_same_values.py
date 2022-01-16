numbers = (float(n) for n in input().split())

numbers_dict = {}

for num in numbers:
    if num not in numbers_dict.keys():
        numbers_dict[num] = 0
    numbers_dict[num] += 1

# for kvp in numbers_dict.items():
#     print(kvp)
#
# print(numbers_dict.items())


for number, count in numbers_dict.items():
    print(f'{number} - {count} times')