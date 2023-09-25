n = int(input())
matrix = [[int(x) for x in input().split()]for _ in range(n)]

primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][n - i - 1] for i in range(n)]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))

# Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
# On the first line, you will receive an integer N - the size of a square matrix.
# The following N lines hold the values for each column - N numbers separated by a single space.
# Print the absolute difference between the primary and the secondary diagonal sums.
#
# Input:
#     3
#     11 2 4
#     4 5 6
#     10 8 -12
# Output:
#     15