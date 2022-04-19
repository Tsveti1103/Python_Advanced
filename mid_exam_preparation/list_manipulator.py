def list_manipulator(numbers, *args):
    command1 = args[0]
    command2 = args[1]
    new_nums = None
    if len(args) > 2:
        new_nums = args[2:]
    if command1 == "add" and command2 == "beginning":
        for num in reversed(new_nums):
            numbers.insert(0, num)
    elif command1 == "add" and command2 == "end":
        for num in new_nums:
            numbers.append(num)
    elif command1 == "remove" and command2 == "beginning":
        if new_nums:
            from_num = int(*new_nums)
            numbers = numbers[from_num:]
        else:
            numbers = numbers[1:]
    elif command1 == "remove" and command2 == "end":
        if new_nums:
            from_num = int(*new_nums)
            numbers = numbers[:-from_num]
        else:
            numbers = numbers[:-1]
    return numbers

print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
