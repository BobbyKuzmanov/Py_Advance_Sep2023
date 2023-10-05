import os

root_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_path, 'my_first_file.txt')
with open(file_path, 'w') as file:
    file.write('I just created my first file!')
    file.close()

# Create a program that creates a file called my_first_file.txt. In that file,
# write a single line with the content: 'I just created my first file!'