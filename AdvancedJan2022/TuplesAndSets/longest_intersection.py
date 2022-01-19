n = int(input())

longest_intersection = []
max_length = 0

for _ in range(n):
    ranges = input().split('-')
    x, y = ranges[0].split(',')
    set_one = set(num for num in range(int(x), int(y) + 1))

    a, b = ranges[1].split(',')
    set_two = set(num for num in range(int(a), int(b) + 1))

    intersection_of_two_ranges = set_one.intersection(set_two)
    if len(intersection_of_two_ranges) >= max_length:
        max_length = len(intersection_of_two_ranges)
        longest_intersection = intersection_of_two_ranges

print(f'Longest intersection is {list(longest_intersection)} with length {max_length}')

