first, second = [int(el) for el in (input().split())]
first_set = set()
second_set = set()
for _ in range(first):
    first_set.add(int(input()))
for _ in range(second):
    second_set.add(int(input()))
result = first_set.intersection(second_set)
print(*result, sep="\n")
