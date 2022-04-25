n = int(input())
counter = 0
odd = set()
even = set()
for _ in range(n):
    name = input()
    counter += 1
    sum_of_char = 0
    for char in name:
        sum_of_char += ord(char)
    sum_of_char //= counter
    if sum_of_char % 2 == 0:
        even.add(sum_of_char)
    else:
        odd.add(sum_of_char)
even_sum = sum(even)
odd_sum = sum(odd)
if even_sum == odd_sum:
    print(*even.union(odd), sep=", ")
elif even_sum > odd_sum:
    print(*even.symmetric_difference(odd), sep=", ")
elif odd_sum > even_sum:
    print(*odd.difference(even), sep=", ")
