from collections import deque

chocolates = [int(el) for el in input().split(", ")]
cups_of_milk = deque([int(el) for el in input().split(", ")])
milkshakes = 0
while chocolates and cups_of_milk and milkshakes < 5:
    current_chocolate = chocolates.pop()
    current_milk = cups_of_milk.popleft()
    if current_chocolate > 0 and current_milk > 0:
        if current_chocolate == current_milk:
            milkshakes += 1
        else:
            cups_of_milk.append(current_milk)
            chocolates.append(current_chocolate - 5)
    else:
        if current_chocolate > 0:
            chocolates.append(current_chocolate)
        if current_milk > 0:
            cups_of_milk.appendleft(current_milk)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join([str(el) for el in chocolates])}")
else:
    print("Chocolate: empty")
if cups_of_milk:
    print(f"Milk: {', '.join([str(el) for el in cups_of_milk])}")
else:
    print("Milk: empty")
