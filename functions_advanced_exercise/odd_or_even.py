command = input()
numbers = [int(el) for el in input().split()]

parity = 0 if command == "Even" else 1
result = sum([x for x in numbers if x % 2 == parity]) * len(numbers)
print(result)
