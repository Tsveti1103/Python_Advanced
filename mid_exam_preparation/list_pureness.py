def best_list_pureness(numbers, k):
    total = {}
    count = 0
    for i in range(k+1):
        current_result = 0
        for index, num in enumerate(numbers):
            current_result += index * num
        if current_result in total.keys():
            continue
        total[current_result] = count
        numbers.insert(0, numbers.pop())
        count += 1
    max_total = max(total.keys())
    return f"Best pureness {max_total} after {total[max_total]} rotations"

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)


