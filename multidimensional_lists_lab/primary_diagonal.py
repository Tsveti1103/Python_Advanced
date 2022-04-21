n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(el) for el in input().split()])
result = 0
for index in range(n):
    result += matrix[index][index]
print(result)