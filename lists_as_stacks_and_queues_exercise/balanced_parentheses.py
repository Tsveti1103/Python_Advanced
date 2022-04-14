parentheses = input()
steck = []
balanced = True
pairs = "(){}[]"
for ch in parentheses:
    if ch in '{([':
        steck.append(ch)
    else:
        if len(steck) == 0:
            balanced = False
            break
        if steck.pop() + ch not in pairs:
            balanced = False
            break

if balanced and len(steck) == 0:
    print("YES")
else:
    print("NO")
