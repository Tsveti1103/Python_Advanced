n = int(input())
result = []
for _ in range(n):
    nums = [int(x) for x in input().split(", ")]
    result.extend(nums)  # result += nums
print(result)

# variant 1
# n = int(input())
# matrix = []
# for _ in range(n):
#     nums = [int(x) for x in input().split(", ")]
#     matrix.append(nums)
# # result = []
# # for row_index in range(len(matrix)):
# #     for col_index in range(len(matrix[row_index])):
# #         result.append(matrix[row_index][col_index])
# # print(result)

# variant 2
# n = int(input())
# matrix = []
# for _ in range(n):
#     nums = [int(x) for x in input().split(", ")]
#     matrix.append(*nums)
# print(matrix)
