def snake_position(matrix):
    for r_index, row in enumerate(matrix):
        for c_index, col in enumerate(row):
            if matrix[r_index][c_index] == "S":
                return r_index, c_index


def movement(move_to, r, c):
    if move_to == "left":
        c -= 1
    elif move_to == "right":
        c += 1
    elif move_to == "up":
        r -= 1
    elif move_to == "down":
        r += 1
    return r, c


def is_out(row, col, m):
    return 0 > row or row >= m or 0 > col or col >= m


def find_b(matrix):
    for r_index, row in enumerate(matrix):
        for c_index, col in enumerate(row):
            if matrix[r_index][c_index] == "B":
                return r_index, c_index


size = int(input())
territory = [[el for el in map(str, input())] for _ in range(size)]
snake_row, snake_col = [int(el) for el in snake_position(territory)]
food_quantity = 0
game_over = False
while True:
    command = input()
    territory[snake_row][snake_col] = "."
    snake_row, snake_col = movement(command, snake_row, snake_col)
    if is_out(snake_row, snake_col, size):
        game_over = True
        break
    if territory[snake_row][snake_col] == "*":
        food_quantity += 1
        if food_quantity == 10:
            break

    if territory[snake_row][snake_col] == "B":
        territory[snake_row][snake_col] = "."
        snake_row, snake_col = [int(el) for el in find_b(territory)]

if game_over:
    print("Game over!")
else:
    print("You won! You fed the snake.")
    territory[snake_row][snake_col] = "S"
print(f"Food eaten: {food_quantity}")
for row in territory:
    print(*row, sep="")
