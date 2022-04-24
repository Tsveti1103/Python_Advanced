from collections import deque


def math(f, opr, s):
    if opr == "*":
        return f * s
    elif opr == "+":
        return f + s
    elif opr == "-":
        return f - s
    elif opr == "/":
        return f // s


text = input().split()
all_operators = "*", "+", "-", "/"
result = 0
numbers = deque()
for char in text:
    if char not in all_operators:
        numbers.append(int(char))
    else:
        while len(numbers) > 1:
            first = numbers.popleft()
            second = numbers.popleft()
            result = math(first, char, second)
            numbers.appendleft(result)
print(result)
