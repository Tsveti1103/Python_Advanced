import sys

rows, cols = [int(x) for x in input().split()]
matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
max_sum = - sys.maxsize
best_row = 0
best_col = 0

for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + matrix[row + 1][col] + \
                      matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + matrix[row + 2][col] + matrix[row + 2][
                          col + 1] + matrix[row + 2][col + 2]
        if current_sum > max_sum:
            max_sum = current_sum
            best_row = row
            best_col = col
print(f"Sum = {max_sum}")
print(f'{matrix[best_row][best_col]} {matrix[best_row][best_col + 1]} {matrix[best_row][best_col + 2]}')
print(f'{matrix[best_row + 1][best_col]} {matrix[best_row + 1][best_col + 1]} {matrix[best_row + 1][best_col + 2]}')
print(f'{matrix[best_row + 2][best_col]} {matrix[best_row + 2][best_col + 1]} {matrix[best_row + 2][best_col + 2]}')
# import sys
#
# rows, cols = [int(el) for el in input().split()]
# matrix = []
# for _ in range(rows):
#     matrix.append([int(el) for el in input().split()])
# max_sum = -sys.maxsize
# max_matrix = []
# for index_r, r in enumerate(matrix):
#     if 0 < index_r < rows - 1:
#         for index_c, c in enumerate(r):
#             if 0 < index_c < cols - 1:
#                 current_sum = matrix[index_r][index_c] + matrix[index_r][index_c + 1] + matrix[index_r][index_c - 1] + \
#                               matrix[index_r + 1][index_c] + matrix[index_r + 1][index_c + 1] + matrix[index_r + 1][
#                                   index_c - 1] + matrix[index_r - 1][index_c] + matrix[index_r - 1][index_c - 1] + \
#                               matrix[index_r - 1][index_c + 1]
#                 if current_sum > max_sum:
#                     max_sum = current_sum
#                     max_matrix = matrix[index_r][index_c]
# print(max_sum)
