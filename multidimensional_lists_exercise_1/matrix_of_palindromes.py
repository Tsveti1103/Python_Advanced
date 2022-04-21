rows, cols = [int(x) for x in input().split()]
matrix = []

for row in range(rows):
    current_row = []
    for col in range(cols):
        first_letter = third_letter = chr(97 + row)
        second_letter = chr(97 + col + row)
        current_letter = first_letter + second_letter + third_letter
        current_row.append(current_letter)
    matrix.append(current_row)
for row in matrix:
    print(*row)
