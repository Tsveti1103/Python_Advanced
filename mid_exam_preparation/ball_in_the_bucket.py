import re


def is_valid(row, col, mat):
    return 0 <= row < mat and 0 <= col < mat


rows = 6
matrix = [[el for el in input().split()] for _ in range(rows)]
points = 0
times = 3
for _ in range(times):
    row, col = [int(el) for el in (re.findall(r'\d+', input()))]
    if is_valid(row, col, rows) and matrix[row][col] == "B":
        matrix[row][col] = 0
        for num in range(rows):
            points += int(matrix[num][col])
prize = None
if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
else:
    if points < 200:
        prize = "Football"
    elif points < 300:
        prize = "Teddy Bear"
    elif points >= 300:
        prize = "Lego Construction Set"
    print(f"Good job! You scored {points} points, and you've won {prize}.")

