from collections import deque

q_pumps = deque()
pumps_count = int(input())
for _ in range(pumps_count):
    pump = [int(p) for p in input().split()]
    q_pumps.append(pump)
counter = 0
while q_pumps:
    truck_fuel = 0
    completed = True
    for pump in q_pumps:
        petrol, distance = pump
        truck_fuel += petrol
        if truck_fuel < distance:
            completed = False
            q_pumps.append(q_pumps.popleft())
            counter += 1
            break
        else:
            truck_fuel -= distance
    if completed:
        print(counter)
        break
