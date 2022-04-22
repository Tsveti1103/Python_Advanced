def is_valid(x, m):
    return 0 <= x < m


presents_count = int(input())
size = int(input())
neighborhood = []
good_kids = 0
for _ in range(size):
    line = input().split()
    neighborhood.append(line)
    for e in line:
        if e == "V":
            good_kids += 1
total_good_kids = good_kids
santa_row = 0
santa_col = 0
santa_fount = False
for row in range(len(neighborhood)):
    for col in range(len(neighborhood)):
        if neighborhood[row][col] == "S":
            santa_row = row
            santa_col = col
            santa_fount = True
            break
    if santa_fount:
        break

while True:
    command = input()
    neighborhood[santa_row][santa_col] = "-"
    if command == "Christmas morning":
        break
    if command == "up" and is_valid(santa_row - 1, size):
        santa_row -= 1

    elif command == "down" and is_valid(santa_row + 1, size):
        santa_row += 1

    elif command == "left" and is_valid(santa_col - 1, size):
        santa_col -= 1

    elif command == "right" and is_valid(santa_col + 1, size):
        santa_col += 1

    if neighborhood[santa_row][santa_col] == "V":
        presents_count -= 1
        good_kids -= 1
        neighborhood[santa_row][santa_col] = "-"
    elif neighborhood[santa_row][santa_col] == "C":
        cookie_effect = []
        cookie_effect += neighborhood[santa_row - 1][santa_col], neighborhood[santa_row + 1][santa_col], \
                         neighborhood[santa_row][santa_col - 1], neighborhood[santa_row][santa_col + 1]
        neighborhood[santa_row - 1][santa_col] = "-"
        neighborhood[santa_row + 1][santa_col] = "-"
        neighborhood[santa_row][santa_col - 1] = "-"
        neighborhood[santa_row][santa_col + 1] = "-"
        for el in cookie_effect:
            if el == "V":
                presents_count -= 1
                good_kids -= 1
            elif el == "X":
                presents_count -= 1
    if presents_count <= 0:
        break
if presents_count <= 0 < good_kids:
    print("Santa ran out of presents!")
for r in neighborhood:
    neighborhood[santa_row][santa_col] = "S"
    print(*r)
if good_kids > 0:
    print(f"No presents for {good_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {total_good_kids - good_kids} happy nice kid/s.")
