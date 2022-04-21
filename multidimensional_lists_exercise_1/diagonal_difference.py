n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])
first_diagonal = []
second_diagonal = []
for row in range(n):
    first_diagonal.append(matrix[row][row])
    second_diagonal.append(matrix[row][n - 1 - row])
first_sum = sum(first_diagonal)
second_sum = sum(second_diagonal)
result = abs(first_sum - second_sum)
print(result)
