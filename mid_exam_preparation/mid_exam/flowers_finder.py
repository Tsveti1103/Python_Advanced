from collections import deque

vowels = deque(input().split())
character = input().split()
flowers = ["rose", "tulip", "lotus", "daffodil"]
f = ["rose", "tulip", "lotus", "daffodil"]
found = False
while vowels and character:
    current_vowel = vowels.popleft()
    current_character = character.pop()
    for index, flower in enumerate(flowers):
        while current_vowel in flower:
            flower = flower.replace(current_vowel, "")
            flowers[index] = flower
        # if current_character in flower:
        while current_character in flower:
            flower = flower.replace(current_character, "")
            flowers[index] = flower
        for i, a in enumerate(flowers):
            if a == "":
                print(f"Word found: {f[i]}")
                found = True
                break
        if found:
            break
    if found:
        break
if not found:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if character:
    print(f"Consonants left: {' '.join(character)}")
