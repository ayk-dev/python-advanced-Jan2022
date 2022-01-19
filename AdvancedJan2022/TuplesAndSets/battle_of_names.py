n = int(input())

odd_scores = set()
even_scores = set()

for i in range(1, n + 1):
    name = list(input())
    ascii_value = sum([ord(ch) for ch in name])
    ascii_value //= i
    if ascii_value % 2 == 0:
        even_scores.add(ascii_value)
    else:
        odd_scores.add(ascii_value)

sum_of_even_scores = sum(even_scores)

sum_of_odd_scores = sum(odd_scores)

result = set()
if sum_of_odd_scores == sum_of_even_scores:
    result = odd_scores.union(even_scores)

elif sum_of_odd_scores > sum_of_even_scores:
    result = odd_scores.difference(even_scores)

elif sum_of_odd_scores < sum_of_even_scores:
    result = odd_scores.symmetric_difference(even_scores)

print(', '.join([str(v) for v in result]))



