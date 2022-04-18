from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])
crafted_presents = {"Gemstone": 0, "Porcelain Sculpture": 0, "Gold": 0, "Diamond Jewellery": 0}
while materials and magic:
    first = materials.pop()
    second = magic.popleft()
    sum_of_m = first + second
    if sum_of_m < 100:
        if sum_of_m % 2 == 0:
            first *= 2
            second *= 3
            sum_of_m = first + second
        else:
            sum_of_m *= 2
    if sum_of_m > 499:
        sum_of_m /= 2
    if 100 <= sum_of_m < 200:
        crafted_presents["Gemstone"] += 1
    elif 200 <= sum_of_m < 300:
        crafted_presents["Porcelain Sculpture"] += 1
    elif 300 <= sum_of_m < 400:
        crafted_presents["Gold"] += 1
    elif 400 <= sum_of_m < 500:
        crafted_presents["Diamond Jewellery"] += 1
if (crafted_presents["Gemstone"] > 0 and crafted_presents["Porcelain Sculpture"] > 0) or \
        (crafted_presents["Gold"] > 0 and crafted_presents["Diamond Jewellery"] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print("Materials left:", ", ".join(str(x) for x in materials))
if magic:
    print("Magic left:",', '.join(str(x) for x in magic))
sorted_presents = sorted(crafted_presents.items(), key=lambda x: x[0])
for present in sorted_presents:
    name, quantity = present
    if quantity > 0:
        print(f"{name}: {quantity}")
