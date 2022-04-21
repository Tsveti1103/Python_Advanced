n = int(input())
first_diagonal = []
second_diagonal = []
for idx in range(n):
    row_element = [int(x) for x in input().split(', ')]
    first_diagonal.append(row_element[idx])
    second_diagonal.append(row_element[n-1-idx])

print(f"Primary diagonal: {', '.join([str(el) for el in first_diagonal])}. Sum: {sum(first_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(el) for el in second_diagonal])}. Sum: {sum(second_diagonal)}")

# n = int(input())
# matrix = []
# for _ in range(n):
#     matrix.append([int(x) for x in input().split(',')])
# first_diagonal = []
# second_diagonal = []
# for row in range(n):
#     first_diagonal.append(matrix[row][row])
#     second_diagonal.append(matrix[row][n - 1 - row])
# print(f"Primary diagonal: {', '.join([str(el) for el in first_diagonal])}. Sum: {sum(first_diagonal)}")
# print(f"Secondary diagonal: {', '.join([str(el) for el in second_diagonal])}. Sum: {sum(second_diagonal)}")


# n = int(input())
# matrix = []
# for _ in range(n):
#     matrix.append([int(x) for x in input().split(',')])
# first_diagonal = []
# second_diagonal = []
# num = n - 1
# for row in range(n):
#     first_diagonal.append(matrix[row][row])
#     second_diagonal.append(matrix[row][num])
#     num -= 1
# first_sum = sum(first_diagonal)
# second_sum = sum(second_diagonal)
# print(f"Primary diagonal: {', '.join([str(el) for el in first_diagonal])}. Sum: {first_sum}")
# print(f"Secondary diagonal: {', '.join([str(el) for el in second_diagonal])}. Sum: {second_sum}")
