n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(input()))
searched_char = input()
position = None
for row_index in range(n):
    for col_index in range(n):
        if searched_char == matrix[row_index][col_index]:
            position = (row_index, col_index)
            print(position)
            break
    if position:
        break
if not position:
    print(f"{searched_char} does not occur in the matrix")

# r = int(input())
# matrix = [list(input()) for _ in range(r)]
# element = input()
# coordinates = None
# for row in matrix:
#     if element in row:
#         coordinates = (matrix.index(row), row.index(element))
#         print(coordinates)
#         break
#
# if not coordinates:
#     print(f"{element} does not occur in the matrix")