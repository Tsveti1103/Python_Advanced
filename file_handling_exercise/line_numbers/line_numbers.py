from string import punctuation

with open('text.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    for row, line in enumerate(input_file):
        striped_line = line.strip()
        letters_count = len([c for c in striped_line if c.isalpha()])
        marks_count = len([el for el in striped_line if el in punctuation])
        output_file.write(f'Line {row + 1}: {striped_line} ({letters_count}) ({marks_count})\n')
