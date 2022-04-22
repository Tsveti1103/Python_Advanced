def is_valid(x):
    return 0 <= x < 5


matrix = []
for _ in range(5):
    matrix.append(input().split())
player_col = 0
player_row = 0
position_found = False
for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "A":
            player_row = row
            player_col = col
            position_found = True
            break
    if position_found:
        break
command_count = int(input())
targets_down = 0
total_targets = 0
targets = []
for line in matrix:
    total_targets += line.count("x")
for _ in range(command_count):
    command_info = input().split()
    command = command_info[0]
    direction = command_info[1]
    if command == "move":
        steps = int(command_info[2])
        if direction == "left" and is_valid(player_col - steps) and matrix[player_row][player_col - steps] == ".":
            player_col -= steps
        if direction == "right" and is_valid(player_col + steps) and matrix[player_row][player_col + steps] == ".":
            player_col += steps
        if direction == "down" and is_valid(player_row + steps) and matrix[player_row + steps][player_col] == ".":
            player_row += steps
        if direction == "up" and is_valid(player_row - steps) and matrix[player_row - steps][player_col] == ".":
            player_row -= steps
    elif command == "shoot":
        if direction == "left":
            for current_col in range(player_col - 1, -1, -1):
                if matrix[player_row][current_col] == "x":
                    targets_down += 1
                    matrix[player_row][current_col] = "."
                    targets.append([player_row, current_col])
                    break
        elif direction == "right":
            for current_col in range(player_col + 1, len(matrix)):
                if matrix[player_row][current_col] == "x":
                    targets_down += 1
                    matrix[player_row][current_col] = "."
                    targets.append([player_row, current_col])
                    break
        elif direction == "up":
            for current_row in range(player_row - 1, -1, -1):
                if matrix[current_row][player_col] == "x":
                    targets_down += 1
                    matrix[current_row][player_col] = "."
                    targets.append([current_row, player_col])
                    break
        if direction == "down":
            for current_row in range(player_row + 1, len(matrix)):
                if matrix[current_row][player_col] == "x":
                    targets_down += 1
                    matrix[current_row][player_col] = "."
                    targets.append([current_row, player_col])
                    break
    if targets_down == total_targets:
        print(f"Training completed! All {targets_down} targets hit.")
        print(*targets, sep="\n")
        break
if total_targets - targets_down > 0:
    print(f"Training not completed! {total_targets - targets_down} targets left.")
    print(*targets, sep="\n")
