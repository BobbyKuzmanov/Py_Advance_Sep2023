rows, columns = [int(x) for x in input().split()]
matrix = [[x for x in input().split()]for _ in range(rows)]

counter = 0

for row in range(rows - 1):
    for col in range(columns - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            counter += 1

print(counter)

# Find the number of all 2x2 squares containing identical chars in a matrix.
# On the first line, you will receive the matrix('s dimensions in the format "{rows} {columns}". '
# In the following rows, you will receive characters separated by a single space.
# Print the number of all square matrices you have found.)
#
# Input:
#     3 4
#     A B B D
#     E B B B
#     I J B B
# Output:
#     2