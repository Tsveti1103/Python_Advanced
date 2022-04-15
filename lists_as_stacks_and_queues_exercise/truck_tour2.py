from collections import deque

q_pumps = deque()
pumps_count = int(input())
for _ in range(pumps_count):
    pump = [int(p) for p in input().split()]
    q_pumps.append(pump)

for attempt in range(pumps_count):
    tank = 0
    failed = False
    for fuel, distance in q_pumps:
        tank += fuel
        if distance > tank:
            failed = True
            break
        else:
            tank -= distance
    if failed:
        q_pumps.append(q_pumps.popleft())
    else:
        print(attempt)
        break
