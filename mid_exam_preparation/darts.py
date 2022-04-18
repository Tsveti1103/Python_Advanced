def is_valid(r, c, m):
    return 0 <= r < m and 0 <= c < m


rows = 7
first_player_name, second_player_name = input().split(", ")
dartboard = [[el for el in input().split()] for _ in range(rows)]
first_player = {"points": 501, "trows": 0}
second_player = {"points": 501, "trows": 0}
turn = 1
while True:
    if first_player["points"] <= 0:
        print(f"{first_player_name} won the game with {first_player['trows']} throws!")
        break
    if second_player["points"] <= 0:
        print(f"{second_player_name} won the game with {second_player['trows']} throws!")
        break
    command_args = input().strip("()").split(", ")
    row = int(command_args[0])
    col = int(command_args[1])

    if turn % 2 == 0:
        current_player = second_player
    else:
        current_player = first_player

    current_player["trows"] += 1
    turn += 1
    if is_valid(row, col, rows):
        current_trow = dartboard[row][col]
        if current_trow.isdigit():
            current_player["points"] -= int(current_trow)
        elif current_trow == "B":
            current_player["points"] = 0
        else:
            score = int(dartboard[row][0]) + int(dartboard[row][-1]) + int(dartboard[0][col]) + int(dartboard[-1][col])
            if current_trow == "D":
                current_player["points"] -= score * 2
            elif current_trow == "T":
                current_player["points"] -= score * 3
