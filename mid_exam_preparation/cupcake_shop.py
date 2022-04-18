def stock_availability(boxes, command, *args):
    inventory_list = []
    for box in boxes:
        inventory_list.append(box)
    if command == "delivery":
        for arg in args:
            inventory_list.append(arg)
    elif command == "sell":
        if args:
            for arg in args:
                if str(arg).isdigit():
                    for box in range(arg):
                        inventory_list.pop(0)
                else:
                    while arg in inventory_list:
                        inventory_list.remove(arg)
        else:
            inventory_list.pop(0)
    return inventory_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

