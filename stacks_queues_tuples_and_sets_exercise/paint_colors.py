from collections import deque

main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}
colors = []
text = deque(input().split())
while text:
    first_substr = text.popleft()
    second_substr = text.pop() if text else ""
    result = first_substr + second_substr
    if result in main_colors or result in secondary_colors:
        colors.append(result)
        continue
    result = second_substr + first_substr
    if result in main_colors or result in secondary_colors:
        colors.append(result)
        continue
    first_substr = first_substr[:-1]
    second_substr = second_substr[:-1]
    if first_substr:
        text.insert(len(text) // 2, first_substr)
    if second_substr:
        text.insert(len(text) // 2, second_substr)
result = []
combinations = {'orange': ['red', 'yellow'], 'purple': ['red', 'blue'], 'green': ['yellow', 'blue']}
for color in colors:
    if color in main_colors:
        result.append(color)
    else:
        is_valid = True
        for color_required in combinations[color]:
            if color_required not in colors:
                is_valid = False
                break
        if is_valid:
            result.append(color)
print(result)
