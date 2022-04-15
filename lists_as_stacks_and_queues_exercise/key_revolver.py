from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(el) for el in input().split()]
locks = deque([int(el) for el in input().split()])
value = int(input())
total_bullets_price = 0
counter = 0
while locks:
    if not bullets:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break
    current_bullet = bullets.pop()
    if current_bullet > locks[0]:
        print("Ping!")
    else:
        print("Bang!")
        locks.popleft()
    total_bullets_price += bullet_price
    counter += 1
    if bullets and counter == gun_barrel_size:
        print("Reloading!")
        counter = 0
if not locks:
    money_earned = value - total_bullets_price
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
