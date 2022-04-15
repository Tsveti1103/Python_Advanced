num_stack = []
count = int(input())
for _ in range(count):
    command = input().split()
    if command[0] == "2" and num_stack:
        num_stack.pop()
    elif command[0] == "3" and num_stack:
        print(max(num_stack))
    elif command[0] == "4" and num_stack:
        print(min(num_stack))
    elif command[0] == "1":
        num = int(command[1])
        num_stack.append(num)
while num_stack:
    element = num_stack.pop()
    if num_stack:
        print(element, end=", ")
    else:
        print(element)
