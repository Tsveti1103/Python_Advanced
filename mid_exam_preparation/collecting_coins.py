def player_position(m):
    for r_index, row in enumerate(m):
        for c_index, col in enumerate(row):
            if col == "P":
                return [r_index, c_index]


def moving(command, r_position, c_position):
    if command == "up":
        r_position -= 1
        if r_position < 0:
            r_position = size - 1
    elif command == "down":
        r_position += 1
        if r_position >= size:
            r_position = 0
    elif command == "left":
        c_position -= 1
        if c_position < 0:
            c_position = size - 1
    elif command == "right":
        c_position += 1
        if c_position >= size:
            c_position = 0
    return r_position, c_position


size = int(input())
field = [[el for el in input().split()] for _ in range(size)]
current_row, current_col = player_position(field)
moves = [player_position(field)]
field[current_row][current_col] = 0
points = 0
win = True
while points < 100:
    command = input()
    position = moving(command, current_row, current_col)
    current_row = position[0]
    current_col = position[1]
    moves.append([current_row, current_col])
    if field[current_row][current_col] == "X":
        points = int(points / 2)
        win = False
        print(f"Game over! You've collected {points} coins.")
        break
    else:
        points += int(field[current_row][current_col])
        field[current_row][current_col] = 0
if win:
    print(f"You won! You've collected {points} coins.")
print("Your path:")
print(*moves, sep="\n")
