rows = int(input())

matrix = []
for i in range(rows):
    row = list(map(int, input(format(i+1)).split(", ")))
    matrix.append(row)

flattened = []
for row in matrix:
    for item in row:
        flattened.append(item)

print(flattened)

# Write a program that receives a matrix and prints the flattened version of it (a list with all the values).
# For example, the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4].
# On the first line, you will receive the number of a matrix
# ('s rows. 'On the next rows, you will get the elements for each column separated with a comma and a space ", ".)
#
# Input:
# 2
# 1, 2, 3
# 4, 5, 6
#
# Output:
# [1, 2, 3, 4, 5, 6]