def is_valid(r, c):
    return 0 <= r < size and 0 <= c < size


def neighbors(row, col, matrix):
    counter = 0
    if is_valid(row, col + 1) and matrix[row][col + 1] == "*":
        counter += 1
    if is_valid(row, col - 1) and matrix[row][col - 1] == "*":
        counter += 1
    if is_valid(row + 1, col) and matrix[row + 1][col] == "*":
        counter += 1
    if is_valid(row - 1, col) and matrix[row - 1][col] == "*":
        counter += 1
    if is_valid(row + 1, col - 1) and matrix[row + 1][col - 1] == "*":
        counter += 1
    if is_valid(row + 1, col + 1) and matrix[row + 1][col + 1] == "*":
        counter += 1
    if is_valid(row - 1, col - 1) and matrix[row - 1][col - 1] == "*":
        counter += 1
    if is_valid(row - 1, col + 1) and matrix[row - 1][col + 1] == "*":
        counter += 1
    return counter


size = int(input())
bombs = int(input())
field = [['0' for i in range(size)] for _ in range(size)]
for _ in range(bombs):
    bomb_row, bomb_col = [int(el) for el in input().strip("()").split(", ")]
    field[bomb_row][bomb_col] = "*"
    for r_index, row in enumerate(field):
        for c_index, col in enumerate(row):
            if field[r_index][c_index] != "*":
                field[r_index][c_index] = neighbors(r_index, c_index, field)
for row in field:
    print(*row)
