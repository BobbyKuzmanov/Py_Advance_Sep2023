rows, columns = [int(x) for x in input().split(", ")]
matrix = []
for _ in range((rows)):
    matrix.append([int(x) for x in input().split()])

for col in range(columns):
    column = [row[col] for row in matrix]
    print(sum(column))


# Write a program that reads a matrix from the console and prints the sum for each column on separate lines.
# On the first line, you will get matrix sizes in the format "{rows}, {columns}". On the next rows,
# you will get elements for each column separated with a single space.
#
# Input:
# 3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0
# Output:
# 12
# 10
# 19
# 20
# 8
# 7
#
# Input:
# 3, 3
# 1 2 3
# 4 5 6
# 7 8 9
# Output:
# 12
# 15
# 18