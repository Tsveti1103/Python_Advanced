def is_valid(x, y, m):
    return 0 <= x < m and 0 <= y < m


def movement(r, c, matrix):
    counter = 0
    if is_valid(r - 2, c + 1, size) and matrix[r - 2][c + 1] == 'K':
        counter += 1
    if is_valid(r - 2, c - 1, size) and matrix[r - 2][c - 1] == 'K':
        counter += 1
    if is_valid(r + 2, c - 1, size) and matrix[r + 2][c - 1] == 'K':
        counter += 1
    if is_valid(r + 2, c + 1, size) and matrix[r + 2][c + 1] == 'K':
        counter += 1
    if is_valid(r + 1, c + 2, size) and matrix[r + 1][c + 2] == 'K':
        counter += 1
    if is_valid(r - 1, c + 2, size) and matrix[r - 1][c + 2] == 'K':
        counter += 1
    if is_valid(r - 1, c - 2, size) and matrix[r - 1][c - 2] == 'K':
        counter += 1
    if is_valid(r + 1, c - 2, size) and matrix[r + 1][c - 2] == 'K':
        counter += 1
    return counter


size = int(input())
board = []

for _ in range(size):
    line = input()
    r = []
    for char in line:
        r.append(char)
    board.append(r)
knights_out = 0
while True:
    max_count = 0
    max_row = 0
    max_col = 0
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "K":
                a = movement(row, col, board)
                if a > max_count:
                    max_count = a
                    max_row = row
                    max_col = col
    if max_count == 0:
        break
    board[max_row][max_col] = 0
    knights_out += 1
print(knights_out)
