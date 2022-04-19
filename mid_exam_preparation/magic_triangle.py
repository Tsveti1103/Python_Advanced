def get_magic_triangle(n):
    matrix = [[1]]
    for row in range(1, n):
        matrix.append([])
        for col in range(row + 1):
            if col == 0:
                up_left = 0
                up_right = matrix[row - 1][col]
            elif col == row:
                up_right = 0
                up_left = matrix[row - 1][col - 1]
            else:
                up_left = matrix[row - 1][col - 1]
                up_right = matrix[row - 1][col]

            matrix[row].append(up_left + up_right)

    return matrix


get_magic_triangle(5)
