rows, _ = [int(el) for el in input().split(", ")]
matrix = []
result = 0
for _ in range(rows):
    cols = [int(x) for x in input().split(", ")]
    matrix.append(cols)
    result += sum(cols)
print(result)
print(matrix)