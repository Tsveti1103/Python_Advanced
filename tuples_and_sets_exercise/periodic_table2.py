n = int(input())
elements = set()
for _ in range(n):
    line = input().split()
    elements = elements.union(line)
print(*elements, sep="\n")
