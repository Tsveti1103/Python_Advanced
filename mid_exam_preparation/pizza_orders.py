from collections import deque

orders = deque(int(el) for el in input().split(", "))
employees = [int(x) for x in input().split(', ')]
total_count = 0

while orders and employees:
    pizza = orders[0]
    current_employee = employees[-1]
    if 0 >= pizza or pizza > 10:
        orders.popleft()

    else:
        if pizza <= current_employee:
            total_count += pizza
            orders.popleft()
            employees.pop()
        else:
            orders[0] -= current_employee
            total_count += current_employee
            employees.pop()


if not orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_count}")
    print(f"Employees: {', '.join([str(x) for x in employees])}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in orders])}")
