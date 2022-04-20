def numbers_searching(*args):
    sorted_ags = sorted(args)
    duplicate_numbers = []
    missing_number = []
    for num in sorted_ags:
        if sorted_ags.count(num) > 1:
            if num not in duplicate_numbers:
                duplicate_numbers.append(num)
            sorted_ags.remove(num)
    for index,num in enumerate(sorted_ags):
        if sorted_ags[index+1] != num + 1:
            missing_number.append(num + 1)
            if missing_number:
                break
    missing_number.append(duplicate_numbers)
    return missing_number


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))

