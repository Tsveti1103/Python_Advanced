# matrix = [[int(el) for el in row_elements.split()] for row_elements in input().split('|')]
#
# flatten_list = [num for sublist in reversed(matrix) for num in sublist]
#
# print(*flatten_list)
final = []
string = input().split("|")
sub_string = []
for sub in string:
    sub_string.append([int(x) for x in sub.split()])
for l in reversed(sub_string):
    for num in l:
        final.append(num)
print(*final)
