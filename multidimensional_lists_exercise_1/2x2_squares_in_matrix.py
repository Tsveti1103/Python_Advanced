rows, cols = [int(el) for el in input().split()]
matrix = []
for _ in range(rows):
    matrix.append(input().split())
counter = 0
for row in range(rows - 1):
    for col in range(cols - 1):
        if matrix[row][col] == matrix[row + 1][col] == matrix[row][col + 1] == matrix[row + 1][col + 1]:
            counter += 1
print(counter)
