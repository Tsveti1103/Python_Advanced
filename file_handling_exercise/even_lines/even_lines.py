characters_to_replace = ["-", ",", ".", "!", "?"]
with open('text.txt', 'r') as file:
    for row, line in enumerate(file):
        if row % 2 == 0:
            result = ' '.join(reversed(line.strip().split()))
            for char in characters_to_replace:
                result = result.replace(char, '@')
            print(result)
