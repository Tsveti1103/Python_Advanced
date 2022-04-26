n = int(input())
guests = set()

for _ in range(n):
    code = input()
    guests.add(code)
guest_code = input()

while not guest_code == "END":
    guests.remove(guest_code)
    guest_code = input()
print(len(guests))
print("\n".join(sorted(guests)))
