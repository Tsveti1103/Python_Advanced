from collections import deque

firework_show = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}
firework_effects = deque(int(el) for el in input().split(", "))
power = [int(el) for el in input().split(", ")]
no_show = True
while firework_effects and power and no_show:

    current_effect = firework_effects[0]
    current_power = power[-1]
    if current_effect <= 0:
        firework_effects.popleft()
        continue
    if current_power <= 0:
        power.pop()
        continue
    current_sum = current_effect + current_power
    if current_sum % 3 == 0 and current_sum % 5 == 0:
        firework_show["Crossette Fireworks"] += 1
        firework_effects.popleft()
        power.pop()
    elif current_sum % 3 == 0:
        firework_show["Palm Fireworks"] += 1
        firework_effects.popleft()
        power.pop()
    elif current_sum % 5 == 0:
        firework_show["Willow Fireworks"] += 1
        firework_effects.popleft()
        power.pop()
    else:
        new_effect = firework_effects.popleft() - 1
        firework_effects.append(new_effect)
    if firework_show["Crossette Fireworks"] >= 3 and firework_show["Palm Fireworks"] >= 3 and firework_show[
        "Willow Fireworks"] >= 3:
        no_show = False
if not no_show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join([str(el) for el in firework_effects])}")
if power:
    print(f"Explosive Power left: {', '.join([str(el) for el in power])}")
for item, value in firework_show.items():
    print(f"{item}: {value}")
