import os

WORKING_PATH_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(WORKING_PATH_DIRECTORY, "numbers.txt")

file = open(file_path, "r")
total = 0

for line in file:
    current_line = int(line)
    total += current_line
    print(total)

file.close()

# Create a program that reads a file and prints the number of characters in it.
# You are given a file called numbers.txt with the following content:
#     1
#     2
#     3
#     4
#     5
# Create a program that reads the numbers from the file.
# Print on the console the sum of those numbers.