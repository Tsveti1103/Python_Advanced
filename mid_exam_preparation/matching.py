from collections import deque

males = [int(el) for el in input().split() if int(el) > 0]
females = deque(int(el) for el in input().split() if int(el) > 0)
matches_count = 0

while males and females:
    current_male = males[-1]
    current_female = females[0]

    if current_female % 25 == 0:
        females.popleft()
        females.popleft()
        continue
    if current_male % 25 == 0:
        males.pop()
        males.pop()
        continue
    if current_male == current_female:
        males.pop()
        females.popleft()
        matches_count += 1
    else:
        females.popleft()
        males.append(males.pop() - 2)
        if males[-1] <= 0:
            males.pop()
print(f"Matches: {matches_count}")
if males:
    reversed_males = reversed(males)
    print(f"Males left: {', '.join(str(el) for el in reversed_males)}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join(str(el) for el in females)}")
else:
    print("Females left: none")
