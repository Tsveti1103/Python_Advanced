from collections import deque

cups = deque(int(el) for el in input().split())
bottles = [int(el) for el in input().split()]
wasted_water = 0

while cups and bottles:
    current_cup = cups[0]
    current_bottle = bottles.pop()
    if current_bottle < current_cup:
        cups[0] -= current_bottle
    else:
        wasted_water += (current_bottle - current_cup)
        cups.popleft()
if bottles:
    print(f"Bottles:", *bottles)
if cups:
    print(f"Cups:", *cups)
print(f"Wasted litters of water: {wasted_water}")
