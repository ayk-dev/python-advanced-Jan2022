from collections import deque


def convert_time_to_seconds(data):
    hours, minutes, seconds = [int(d) for d in data.split(':')]
    result = seconds + minutes * 60 + hours * 60 * 60
    return result


def convert_seconds_to_time(sec):
    sec %= 24 * 60 * 60
    hours = sec // 3600
    minutes = (sec - hours * 3600) // 60
    seconds = sec - hours * 3600 - minutes * 60
    return "%02i:%02i:%02i" % (hours, minutes, seconds)


robots_queue = deque(input().split(';'))

process_time_by_robot = {}
busy_time_by_robot = {}

for robot in robots_queue:
    name, time = robot.split('-')
    process_time_by_robot[name] = int(time)
    busy_time_by_robot[name] = -1

seconds = convert_time_to_seconds(input())

items = deque()

product = input()
while not product == 'End':
    items.append(product)
    product = input()

while items:
    seconds = seconds + 1
    product = items.popleft()
    for name, busy_until in busy_time_by_robot.items():
        if seconds >= busy_until:
            time_str = convert_seconds_to_time(seconds)
            print(f'{name} - {product} [{time_str}]')
            busy_time_by_robot[name] = seconds + process_time_by_robot[name]
            break
    else:
        items.append(product)



