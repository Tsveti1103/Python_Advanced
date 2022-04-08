from os import walk

files_by_extension = {}
for _, _, files in walk(''):
    for file in files:
        extension = file.split('.')[-1]
        if extension not in files_by_extension:
            files_by_extension[extension] = []
        files_by_extension[extension].append(file)

with open('result.txt', 'w') as output:
    for ext, files in sorted(files_by_extension.items()):
        output.write(f".{ext}\n")
        for file in sorted(files):
            output.write(f'- - - {file}\n')
