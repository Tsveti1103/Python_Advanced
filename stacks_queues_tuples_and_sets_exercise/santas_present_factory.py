from collections import deque

materials_box = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())
toys = {400: {"Name": "Bicycle", "count": 0}, 150: {"Name": "Doll", "count": 0},
        300: {"Name": "Teddy bear", "count": 0}, 250: {"Name": "Wooden train", "count": 0}}
while materials_box and magic_level:
    current_box = materials_box.pop()
    current_magic = magic_level.popleft()
    result = current_box * current_magic
    if result in toys.keys():
        toys[result]["count"] += 1
    else:
        if result < 0:
            materials_box.append(current_box + current_magic)
        elif result > 0:
            materials_box.append(current_box + 15)
        else:
            if current_box == 0 and current_magic == 0:
                continue
            if current_magic == 0:
                materials_box.append(current_box)
            else:
                magic_level.appendleft(current_magic)
if (toys[150]["count"] > 0 and toys[250]["count"] > 0) or (toys[300]["count"] > 0 and toys[400]["count"] > 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials_box:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials_box)])}")
if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")
for toy in toys.values():
    if toy["count"] > 0:
        print(f"{toy['Name']}: {toy['count']}")
