data = input().split(", ")
rows = int(data[0])
columns = int(data[1])

matrix = []
for _ in range(rows):
    elements = [int(x) for x in input().split(", ")]
    matrix.append(elements)

sums_nums = 0

for row_index in range(rows):
    for col_index in range(columns):
        sums_nums += matrix[row_index][col_index]

print(sums_nums)
print(matrix)

# Write a program that reads a matrix from the console and prints:
#     • The sum of all numbers in the matrix
#     • The matrix itself
# On the first line, you will receive the matrix sizes in the format "{rows}, {columns}". On the next rows,
# you will get elements for each column separated by a comma and a space ", ".
#
# Input:
# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
# Output:
# 76
# [[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]
