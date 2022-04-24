from collections import deque


def math(a, op, b):
    if op == "+":
        return abs(a + b)
    elif op == "-":
        return abs(a - b)
    elif op == "*":
        return abs(a * b)
    elif op == "/":
        if b != 0:
            return abs(a / b)
        else:
            return 0


bees = deque([int(el) for el in input().split()])
nectar = [int(el) for el in input().split()]
symbols = deque(input().split())
total_honey = 0
while bees and nectar:
    current_bee = bees[0]
    current_nectar = nectar.pop()
    if current_nectar >= current_bee:
        operator = symbols.popleft()
        total_honey += math(current_bee, operator, current_nectar)
        bees.popleft()
print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join([str(b) for b in bees])}")
elif nectar:
    print(f"Nectar left: {', '.join([str(b) for b in nectar])}")
