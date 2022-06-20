from collections import deque

def fill_the_box(*args):
    height = args[0]
    length = args[1]
    width = args[2]
    free_space = height * length * width

    no_more_space = False
    cubes = deque(args[3:])
    while cubes:
        current = cubes.popleft()
        if current == 'Finish':
            break

        cube = int(current)
        if free_space >= cube:
            free_space -= cube
        else:
            cubes.appendleft(cube - free_space)
            free_space = 0
            no_more_space = True
            break
    result = ''
    if no_more_space:
         result = f'No more free space! You have {sum([int(x) for x in cubes if x != "Finish"])} more cubes.'
    else:
        result = f'There is free space in the box. You could put {free_space} more cubes.'

    return result


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))