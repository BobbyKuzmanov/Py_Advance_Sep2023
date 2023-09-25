r, c = [int(x) for x in input().split()]

start = ord('a')

for row in range(r):
    for col in range(c):
        print(f"{chr(start + row)}{chr(start + row + col)}{chr(start + row)}", end=' ')
    print()

# Write a program to generate the following matrix of palindromes of 3 letters with r rows and
# c columns like the one in the examples below.
#     • Rows define the first and the last letter: row 0  'a', row 1  'b', row 2  'c', …
#     • Columns + rows define the middle letter:
#         ◦ column 0, row 0  'a', column 1, row 0  'b', column 2, row 0  'c', …
#         ◦ column 0, row 1  'b', column 1, row 1  'c', column 2, row 1  'd', …
# Input
#     • The numbers r and c stay at the first line at the input in the format "{rows} {columns}"
#     • r and c are integers in the range [1, 26]
# Examples
# Input	    Output
# 3 2         aaa aba
#             bbb bcb
#             ccc cdc