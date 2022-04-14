clothes = input().split()
rack_capacity = int(input())
rack_count = 1
sum_of_clothes = 0
while clothes:
    current_clothes = int(clothes.pop())
    sum_of_clothes += current_clothes
    if sum_of_clothes > rack_capacity:
        rack_count += 1
        sum_of_clothes = current_clothes
print(rack_count)
