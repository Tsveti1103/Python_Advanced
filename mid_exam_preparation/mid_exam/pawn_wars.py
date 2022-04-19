def white_position(matrix):
    for r_index, row in enumerate(matrix):
        for c_index, col in enumerate(row):
            if matrix[r_index][c_index] == "w":
                return r_index, c_index


def black_positions(matrix):
    for r_index, row in enumerate(matrix):
        for c_index, col in enumerate(row):
            if matrix[r_index][c_index] == "b":
                return r_index, c_index


def is_inside(n, s):
    return 0 <= n < len(s)


def white_is_winner(r, c, matrix):
    if is_inside(r - 1, matrix) and (is_inside(c + 1, matrix) or is_inside(c - 1, matrix)):
        return matrix[r - 1][c + 1] == "b" or matrix[r - 1][c - 1] == "b"


def black_is_winner(r, c, matrix):
    if is_inside(r + 1, matrix) and (is_inside(c + 1, matrix) or is_inside(c - 1, matrix)):
        return matrix[r + 1][c + 1] == "w" or matrix[r + 1][c - 1] == "w"


size = 8
chessboard = [[el for el in input().split()] for _ in range(size)]
columns = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}
rows = {0: 8, 1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}
white_row, white_col = white_position(chessboard)
black_row, black_col = black_positions(chessboard)
count = 1
while True:
    if count % 2 != 0:
        if white_is_winner(white_row, white_col, chessboard):
            print(f"Game over! White win, capture on {columns[black_col]}{rows[black_row]}.")
            break
        else:
            if is_inside(white_row + 1, chessboard):
                white_row -= 1
            if white_row == 0:
                print(f"Game over! White pawn is promoted to a queen at {columns[white_col]}{rows[white_row]}.")
                break
    else:
        if black_is_winner(black_row, black_col, chessboard):
            print(f"Game over! Black win, capture on {columns[white_col]}{rows[white_row]}.")
            break
        else:
            if is_inside(black_row + 1, chessboard):
                black_row += 1
            if black_row == 7:
                print(f"Game over! Black pawn is promoted to a queen at {columns[black_col]}{rows[black_row]}.")
                break

    count += 1
