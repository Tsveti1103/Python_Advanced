from os import listdir, path


def traverse_dir(current_path, files_by_ext):
    for element in listdir(current_path):
        if path.isdir(path.join(current_path, element)):
            traverse_dir(path.join(current_path, element), files_by_ext)
        else:
            extension = element.split(".")[-1]
            if extension not in files_by_extension:
                files_by_extension[extension] = []
            files_by_extension[extension].append(element)


files_by_extension = {}
traverse_dir('', files_by_extension)
for ext, files in sorted(files_by_extension.items()):
    print(f".{ext}")
    for file in sorted(files):
        print(f'- - - {file}')
