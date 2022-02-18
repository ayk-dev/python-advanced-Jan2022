def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


n = int(input())

moves = input().split()
field = []
miner = []
total_coal = 0
for i in range(n):
    row = input().split()
    field.append(row)
    if 's' in row:
        miner_col = row.index('s')
        miner = [i, miner_col]
    total_coal += row.count('c')

coal_collected = 0
game_over = False
for move in moves:
    new_position = []
    if move == "up":
        new_position = [miner[0] - 1, miner[1]]
    elif move == "right":
        new_position = [miner[0], miner[1] + 1]
    elif move == "left":
        new_position = [miner[0], miner[1] - 1]
    elif move == "down":
        new_position = [miner[0] + 1, miner[1]]
    if is_inside(new_position[0], new_position[1], n):
        field[miner[0]][miner[1]] = '*'
        miner = [new_position[0], new_position[1]]

        if field[miner[0]][miner[1]] == 'c':
            coal_collected += 1
            field[miner[0]][miner[1]] = '*'

        elif field[miner[0]][miner[1]] == 'e':
            game_over = True
            break

if game_over:
    print(f'Game over! ({miner[0]}, {miner[1]})')
else:
    if coal_collected == total_coal:
        print(f'You collected all coal! ({miner[0]}, {miner[1]})')
    else:
        remaining_coal = total_coal - coal_collected
        print(f'{remaining_coal} pieces of coal left. ({miner[0]}, {miner[1]})')


