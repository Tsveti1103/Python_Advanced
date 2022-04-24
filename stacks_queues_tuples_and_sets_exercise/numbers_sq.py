first = set([int(el) for el in input().split()])
second = set([int(el) for el in input().split()])
n = int(input())
for _ in range(n):
    command = input().split()
    numbers = set([int(el) for el in command[2:]])
    if command[0] == "Add":
        if command[1] == "First":
            first = first.union(numbers)
        elif command[1] == "Second":
            second = second.union(numbers)
    elif command[0] == "Remove":
        if command[1] == "First":
            first = first.difference(numbers)
        elif command[1] == "Second":
            second = second.difference(numbers)
    elif command[0] == "Check":
        if first.issubset(second) or second.issubset(first):
            print(True)
        else:
            print(False)
print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")
