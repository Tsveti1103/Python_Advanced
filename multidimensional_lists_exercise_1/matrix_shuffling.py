def is_outside(row, col, f_rows, f_cols):
    return row < 0 or col < 0 or row >= f_rows or col >= f_cols


rows, cols = [int(x) for x in input().split()]

matrix = []
for _ in range(rows):
    matrix.append(input().split())

while True:
    line = input()
    if line == "END":
        break
    command_args = line.split()
    if len(command_args) != 5 or command_args[0] != "swap":
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in command_args[1:]]

    if is_outside(row1, col1, rows, cols) or is_outside(row2, col2, rows, cols):
        print("Invalid input!")
        continue
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    for m_row in matrix:
        print(*m_row, sep=" ")
