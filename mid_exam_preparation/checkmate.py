def king_position(matrix):
    for r_index, row in enumerate(matrix):
        for c_index, col in enumerate(row):
            if matrix[r_index][c_index] == "K":
                return r_index, c_index


def find_queen(matrix):
    for r_index, row in enumerate(matrix):
        for c_index, col in enumerate(row):
            if matrix[r_index][c_index] == "Q":
                matrix[r_index][c_index] = "C"
                return [r_index, c_index]


def queen_movement(current_queen, matrix):
    q_row, q_col = current_queen
    move_up = []
    move_down = []
    move_left = []
    move_right = []
    right_up = []
    right_down = []
    left_up = []
    left_down = []
    for u in range(q_row, -1, -1):
        row = q_row - 1
        move_up.append(matrix[row][q_col])
        if matrix[row][q_col] == "K":
            break
    for d in range(q_row, len(matrix)):
        row = q_row + 1
        move_down.append((matrix[row][q_col]))
        if matrix[row][q_col] == "K":
            break
    for l in range(q_col, -1, -1):
        col = q_col - 1
        move_left.append(matrix[q_row][col])
        if matrix[q_row][col] == "K":
            break
    for r in range(q_col, len(matrix)):
        col = q_col + 1
        move_right.append(matrix[q_row][col])
        if matrix[q_row][col] == "K":
            break

size = 8
board = [[el for el in input().split()] for _ in range(size)]
king_row, king_col = king_position(board)
queens = []
wining_queens = []
for row in board:
    if "Q" in row:
        queens.append(find_queen(board))
for queen in queens:
    queen_movement(queen, board)
