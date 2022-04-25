text = input()
s_text = sorted(set(text))
t_text = tuple(text)
for el in s_text:
    print(f"{el}: {text.count(el)} time/s")
