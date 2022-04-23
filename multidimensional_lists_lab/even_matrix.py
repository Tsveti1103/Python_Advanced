print([[int(el) for el in input().split(", ") if int(el) % 2 == 0] for _ in range(int(input()))])

# variant 1
# matrix = [[int(el) for el in input().split(", ") if int(el) % 2 == 0] for _ in range(int(input()))]
# print(matrix)

# variant 2
# rows = int(input())
# matrix = []
# for _ in range(rows):
#     row = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
#     matrix.append(row)
# print(matrix)

# variant 3
# rows = int(input())
# matrix = []
# row = [[int(el) for el in input().split(", ") if int(el) % 2 == 0] for _ in range(rows)]
# matrix.append(row)
# print(*matrix)
