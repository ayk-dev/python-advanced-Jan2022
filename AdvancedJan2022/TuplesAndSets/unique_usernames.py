n = int(input())

unique_username = set()

for _ in range(n):
    unique_username.add(input())

print('\n'.join(unique_username))