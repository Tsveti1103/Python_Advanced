n = int(input())
intersection = []
for _ in range(n):
    first_set = set()
    second_set = set()
    first_line, second_line = input().split("-")
    first_line_start, first_line_end = [int(el) for el in first_line.split(",")]
    second_line_start, second_line_end = [int(el) for el in second_line.split(",")]
    for num in range(first_line_start, first_line_end + 1):
        first_set.add(num)
    for num in range(second_line_start, second_line_end + 1):
        second_set.add(num)
    current_intersection = first_set.intersection(second_set)
    if len(current_intersection) > len(intersection):
        intersection = list(current_intersection)
print(f"Longest intersection is {intersection} with length {len(intersection)}")
