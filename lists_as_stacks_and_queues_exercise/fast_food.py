from collections import deque

total_food = int(input())
orders = deque([int(x) for x in input().split()])
biggest_order = max(orders)
print(biggest_order)

while orders:
    current_order = orders[0]
    if current_order > total_food:
        break
    total_food -= current_order
    orders.popleft()

if orders:
    print("Orders left:", *orders)
else:
    print("Orders complete")
