n = int(input())

matrix = []
bunny = []

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "B":
            bunny = [row, col]

possible_moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
max_eggs = float('-inf')
max_direction = ''
max_eggs_matrix = []

for direction, move in possible_moves.items():
    eggs = 0
    curr_eggs_matrix = []
    row =  bunny[0] + move[0]
    col = bunny[1] + move[1]

    while 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == "X":
            break
        eggs += int(matrix[row][col])
        curr_eggs_matrix.append([row, col])
        row += move[0]
        col += move[1]

    if eggs > max_eggs and curr_eggs_matrix:
        max_eggs = eggs
        max_direction = direction
        max_eggs_matrix = curr_eggs_matrix

print(max_direction)

for el in max_eggs_matrix:
    print(el)

print(max_eggs)


# Your task is to collect as many eggs as possible.
# On the first line, you will be given a number representing the size of the field.
# On the following few lines, you will be given a field with:
#     • One bunny - randomly placed in it and marked with the symbol "B"
#     • Number of eggs placed at different positions of the field and traps marked with "X"
# Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs.
# he directions that should be considered as possible are up, down, left, and right.
# If you reach a trap while checking some of the directions,
# you should not consider the fields after the trap in this direction. For more clarifications, see the examples below.
# Note: Consider ONLY the paths from which the bunny has collected 1 or more eggs.
# Input
#     • A number representing the size of the field
#     • The matrix representing the field (each position separated by a single space)
# Output
#     • The direction which should be considered as best (lowercase)
#     • The field positions from which we are collecting eggs as lists
#     • The total number of eggs collected
# Constraints
#     • There will NOT be two or more paths consisting of the same total amount of eggs.
#
# Input:
#     5
#     1 3 7 9 11
#     X 5 4 X 63
#     7 3 21 95 1
#     B 1 73 4 9
#     9 2 33 2 0

# Output:
#     right
#     [3, 1]
#     [3, 2]
#     [3, 3]
#     [3, 4]
#     87
