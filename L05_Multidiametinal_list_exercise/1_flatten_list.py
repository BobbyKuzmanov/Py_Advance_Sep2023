strings = input().split("|")

matrix = []

for i in range(len(strings) - 1, -1, -1):
    row = [int(x) for x in strings[i].split()]
    if row:
        matrix.append(row)

for row in matrix:
    print(*row, sep=" ", end=" ")
# print(*[x for row in matrix for x in row])

# Write a program to flatten several lists of numbers received in the following format:
#      String with numbers or empty strings separated by "|"
#      Values are separated by spaces (" ", one or several)
#      Order the output list from the last to the first matrix sub-lists
#       and their values from left to right as shown below

# Input:
# 1 2 3 |4 5 6 |  7  88
# Output:
# 7 88 4 5 6 1 2 3
