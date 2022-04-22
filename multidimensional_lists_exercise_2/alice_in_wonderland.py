def is_inside(x, matrix):
    return 0 <= x < matrix


size = int(input())
territory = []
tea_quantity = 0
alice_row = 0
alice_col = 0
alice_found = False
for _ in range(size):
    territory.append(input().split())

for row in range(len(territory)):
    for col in range(len(territory)):
        if territory[row][col] == "A":
            alice_col = col
            alice_row = row
            alice_found = True
            break
    if alice_found:
        break
game_over = False
while True:
    command = input()
    territory[alice_row][alice_col] = "*"
    if command == "up":
        if is_inside(alice_row - 1, size):
            alice_row -= 1
            if territory[alice_row][alice_col].isdigit():
                tea_quantity += int(territory[alice_row][alice_col])
        else:
            game_over = True
    elif command == "down":
        if is_inside(alice_row + 1, size):
            alice_row += 1
            if territory[alice_row][alice_col].isdigit():
                tea_quantity += int(territory[alice_row][alice_col])
        else:
            game_over = True
    elif command == "left":
        if is_inside(alice_col - 1, size):
            alice_col -= 1
            if territory[alice_row][alice_col].isdigit():
                tea_quantity += int(territory[alice_row][alice_col])
        else:
            game_over = True
    elif command == "right":
        if is_inside(alice_col + 1, size):
            alice_col += 1
            if territory[alice_row][alice_col].isdigit():
                tea_quantity += int(territory[alice_row][alice_col])
        else:
            game_over = True
    if territory[alice_row][alice_col] == "R" or game_over:
        territory[alice_row][alice_col] = "*"
        print("Alice didn't make it to the tea party.")
        for line in territory:
            print(*line)
        break
    if tea_quantity >= 10:
        territory[alice_row][alice_col] = "*"
        print("She did it! She went to the party.")
        for line in territory:
            print(*line)
        break
