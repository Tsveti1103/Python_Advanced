def is_valid(x, r):
    return 0 <= x < r


rows = int(input())
matrix = []
for _ in range(rows):
    line = [int(x) for x in input().split()]
    matrix.append(line)
while True:
    command_info = input().split()
    if command_info[0] == "END":
        break
    command, row, col, value = command_info
    row = int(row)
    col = int(col)
    value = int(value)
    if is_valid(row, rows) and is_valid(col, rows):
        if command == "Add":
            matrix[row][col] += value
        elif command == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")
for row in matrix:
    print(*row)
