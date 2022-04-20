from collections import deque

customers = deque([int(el) for el in input().split(", ")])
taxis = [int(el) for el in input().split(", ")]
total_time = 0

while customers and taxis:
    current_customer = customers[0]
    current_taxi = taxis[-1]
    if current_taxi >= current_customer:
        customers.popleft()
        taxis.pop()
        total_time += current_customer
    else:
        taxis.pop()
if customers:
    print("Not all customers were driven to their destinations")
    print("Customers left:", ', '.join(str(el) for el in customers))
else:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
