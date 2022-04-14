clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
rack_count = 1
current_rack = rack_capacity
while clothes:
    current_piece = clothes[-1]
    if current_piece <= current_rack:
        clothes.pop()
        current_rack -= current_piece
    else:
        rack_count += 1
        current_rack = rack_capacity
print(rack_count)
