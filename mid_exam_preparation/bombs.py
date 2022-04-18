from collections import deque


def pouch_is_full(one, two, three):
    return one >= 3 and two >= 3 and three >= 3


bomb_effects = deque(int(el) for el in input().split(", "))
bomb_casings = [int(el) for el in input().split(", ")]
pouch = {60: {"count": 0, "name": "Cherry Bombs"}, 40: {"count": 0, "name": "Datura Bombs"},
         120: {"count": 0, "name": "Smoke Decoy Bombs"}}
full_pouch = False
while bomb_effects and bomb_casings:
    current_sum = bomb_effects[0] + bomb_casings[-1]
    if current_sum in pouch:
        pouch[current_sum]["count"] += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5
    if pouch_is_full(pouch[40]["count"], pouch[60]["count"], pouch[120]["count"]):
        full_pouch = True
        break
if not bomb_effects:
    bomb_effects = ["empty"]
if not bomb_casings:
    bomb_casings = ["empty"]

if full_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

print("Bomb Effects:", ', '.join(map(str, bomb_effects)))
print("Bomb Casings:", ', '.join(map(str, bomb_casings)))
for bomb in pouch.values():
    print(f"{bomb['name']}: {bomb['count']}")
