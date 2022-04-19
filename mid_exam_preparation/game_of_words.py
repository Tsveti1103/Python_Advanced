def player_position(matrix):
    for r_index, row in enumerate(matrix):
        for c_index, col in enumerate(row):
            if matrix[r_index][c_index] == "P":
                matrix[r_index][c_index] = "-"
                return r_index, c_index


def moving(move, row, col):
    if move == "up":
        row -= 1
    elif move == "down":
        row += 1
    elif move == "left":
        col -= 1
    elif move == "right":
        col += 1
    return row, col


def is_out(r, c):
    return 0 > r or r >= size or 0 > c or c >= size


word = input()
size = int(input())
field = [[el for el in map(str, input())] for _ in range(size)]
commands_count = int(input())
player_row, player_col = player_position(field)
for _ in range(commands_count):
    command = input()
    new_row, new_col = moving(command, player_row, player_col)
    if is_out(new_row, new_col):
        if word:
            word = word[:-1]
        new_row, new_col = player_row, player_col
    if field[new_row][new_col] != "-":
        word += field[new_row][new_col]
        field[new_row][new_col] = "-"
    player_row, player_col = new_row, new_col
field[player_row][player_col] = "P"
print(word)
for line in field:
    print(*line, sep="")
