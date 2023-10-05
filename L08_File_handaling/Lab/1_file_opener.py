import os

root_path = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join(root_path, 'files')
file_path = os.path.join(files_dir, 'text.txt')

if os.path.isfile(file_path):
    print('File found')
else:
    print('File not found')


# import os
#
# WORKING_PATH_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(WORKING_PATH_DIRECTORY, "text.txt")
#
# try:
#     file = open("text.txt", "r")
#     print("File found")
#     file.close()
# except:
#     print("File not found")

# You are given a file called text.txt with the following text:
#     This some random line
#     This is second line
#     And another line
# Create a program that opens the file.
# If the file is found, print 'File found'.
# If the file is not found, print 'File not found'.
