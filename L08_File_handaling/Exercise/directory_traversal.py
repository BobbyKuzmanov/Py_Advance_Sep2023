import os


def save_extensions(dir_name, first_level=False):  #
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)  # dir_name + / + filename

        if os.path.isfile(file):
            extension = filename.split('.')[-1]

            if extension not in extensions:
                extensions[extension] = []

            extensions[extension].append(filename)

        if os.path.isdir(file) and not first_level:
            save_extensions(file)
            save_extensions(file, first_level=True)


directory = input()
extensions = {}  # examples: { ".py": ["file1.py", "file2.py"]}
result = []
save_extensions(directory)

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    result.append(f' .{extension}')

    for file in files:
        result.append(f'- - - {file}')

with open('files/report.txt', 'w') as file:
    file.write('\n'.join(result))
