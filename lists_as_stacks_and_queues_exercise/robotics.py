from collections import deque


def convert_str_to_seconds(str_time):
    hours, minutes, seconds = [int(x) for x in str_time.split(':')]
    return hours * 60 * 60 + minutes * 60 + seconds


def convert_seconds_to_str_time(seconds):
    seconds %= 24 * 60 * 60
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


robots_data = input().split(';')
robots = {}

for robot in robots_data:
    name, process_time = robot.split('-')
    robots[name] = {"process_time": int(process_time), "busy_until": -1}
time = convert_str_to_seconds(input())
items = deque()

while True:
    line = input()
    if line == 'End':
        break
    items.append(line)

while items:
    time += 1
    item = items.popleft()

    for name, characteristics in robots.items():
        if time >= robots[name]["busy_until"]:
            robots[name]["busy_until"] = time + robots[name]["process_time"]
            print(f'{name} - {item} [{convert_seconds_to_str_time(time)}]')
            break
    else:
        items.append(item)
