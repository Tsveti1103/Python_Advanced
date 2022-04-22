def is_valid(x, m):
    return 0 <= x < m


size = int(input())
field = []
for _ in range(size):
    field.append(input().split())
bunny_row = 0
bunny_col = 0
for row in range(len(field)):
    for col in range(len(field)):
        if field[row][col] == "B":
            bunny_row = row
            bunny_col = col
right = 0
left = 0
up = 0
down = 0
right_m = []
left_m = []
up_m = []
down_m = []
directions_info = {"right": {"sum": 0, "coords": []},
                   "left": {"sum": 0, "coords": []},
                   "down": {"sum": 0, "coords": []},
                   "up": {"sum": 0, "coords": []}}
for r in range(1, len(field)):
    if is_valid(bunny_col + r, size):
        if field[bunny_row][bunny_col + r] != "X":
            right += int(field[bunny_row][bunny_col + r])
            right_m.append([bunny_row, bunny_col + r])
        else:
            break
    directions_info["right"]["sum"] = right
    directions_info["right"]["coords"] = right_m

for le in range(1, len(field)):
    if is_valid(bunny_col - le, size):
        if field[bunny_row][bunny_col - le] != "X":
            left += int(field[bunny_row][bunny_col - le])
            left_m.append([bunny_row, bunny_col - le])
        else:
            break
    directions_info["left"]["sum"] = left
    directions_info["left"]["coords"] = left_m

for u in range(1, len(field)):
    if is_valid(bunny_row - u, size):
        if field[bunny_row - u][bunny_col] != "X":
            up += int(field[bunny_row - u][bunny_col])
            up_m.append([bunny_row - u, bunny_col])
        else:
            break
    directions_info["up"]["sum"] = up
    directions_info["up"]["coords"] = up_m

for d in range(1, len(field)):
    if is_valid(bunny_row + d, size):
        if field[bunny_row + d][bunny_col] != "X":
            down += int(field[bunny_row + d][bunny_col])
            down_m.append([bunny_row + d, bunny_col])
        else:
            break
    directions_info["down"]["sum"] = down
    directions_info["down"]["coords"] = down_m
max = max(up, down, left, right)
for k, v in directions_info.items():
    if v["sum"] == max:
        print(k)
        print(*v["coords"], sep='\n')
        print(max)
        break
