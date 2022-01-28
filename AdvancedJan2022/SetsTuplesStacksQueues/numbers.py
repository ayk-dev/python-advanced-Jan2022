seq_one = set(int(x) for x in input().split())
seq_two = set(int(x) for x in input().split())

n = int(input())

for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'Add':
        if cmd[1] == 'First':
            [seq_one.add(int(num)) for num in cmd[2:]]
        elif cmd[1] == 'Second':
            [seq_two.add(int(num)) for num in cmd[2:]]

    elif cmd[0] == 'Remove':
        set_to_remove = set()
        set_to_remove.update(int(n) for n in cmd[2:])

        if cmd[1] == 'First':
            seq_one = seq_one.difference(set_to_remove)
        elif cmd[1] == 'Second':
            seq_two = seq_two.difference(set_to_remove)

    elif cmd[0] == 'Check':
        is_subset = seq_one.issubset(seq_two) or seq_two.issubset(seq_one)
        print(is_subset)

print(*sorted(seq_one), sep=', ')
print(*sorted(seq_two), sep=', ')
