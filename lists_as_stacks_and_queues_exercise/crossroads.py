from collections import deque

green_light = int(input())
free_window = int(input())
cars = deque()
command = input()
cars_passed = 0
crash = False
while command != "END":
    if command != "green":
        cars.append(command)
    else:
        current_green = green_light
        while cars and current_green > 0:
            current_car = cars.popleft()
            if len(current_car) <= current_green or current_green + free_window >= len(current_car):
                current_green -= len(current_car)
                cars_passed += 1
            else:
                crash = True
                crash_at = current_car[current_green + free_window]
                print("A crash happened!")
                print(f"{current_car} was hit at {crash_at}.")
                break
    if crash:
        break
    command = input()
if not crash:
    print("Everyone is safe.")
    print(f"{cars_passed} total cars passed the crossroads.")
