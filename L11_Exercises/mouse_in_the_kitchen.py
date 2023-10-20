def is_valid(value, max_value):
    return 0 <= value < max_value


def next_move(command, current_row, current_col):
    if command == 'up' and is_valid(current_row-1, rows):
        return current_row-1, current_col
    if command == 'down' and is_valid(current_row+1, rows):
        return current_row+1, current_col
    if command == 'left' and is_valid(current_col-1, cols):
        return current_row, current_col-1
    if command == 'right' and is_valid(current_col+1, cols):
        return current_row, current_col+1
    return None, None


rows, cols = [int(x) for x in input().split(',')]
field = []
mouse_row, mouse_col = None, None
cheese_cnt = 0
line = ''

for r in range(rows):
    row = list(input())
    field.append(row)
    if 'M' in row:
        mouse_row = r
        mouse_col = row.index('M')
    if 'C' in row:
        cheese_cnt += row.count('C')


while cheese_cnt != 0:
    line = input()
    if line == 'danger':
        break
    next_row, next_col = next_move(line, mouse_row, mouse_col)
    if next_row is None or next_col is None:
        print('No more cheese for tonight!')
        break
    if field[next_row][next_col] == '@':
        continue
    if field[next_row][next_col] == 'T':
        field[mouse_row][mouse_col] = '*'
        mouse_row, mouse_col = next_row, next_col
        field[mouse_row][mouse_col] = 'M'
        print("Mouse is trapped!")
        break
    if field[next_row][next_col] == '*':
        field[mouse_row][mouse_col] = '*'
        mouse_row, mouse_col = next_row, next_col
        field[mouse_row][mouse_col] = 'M'
        continue
    if field[next_row][next_col] == 'C':
        cheese_cnt -= 1
        field[mouse_row][mouse_col] = '*'
        mouse_row, mouse_col = next_row, next_col
        field[mouse_row][mouse_col] = 'M'

else:
    print("Happy mouse! All the cheese is eaten, good night!")

if cheese_cnt and line == 'danger':
    print("Mouse will come back later!")

for row in field:
    print(''.join(row))

# In the beginning, you will be given N and M – integers, separated by a comma - ",",
# indicating the cupboard’s area dimensions. On the next N lines, you will receive strings,
# representing the rows of the area, with M columns.
# After that, on each line, until the command "danger" appears as an input string,
# you will receive the possible directions for the mouse to move - "up", "down", "right", and "left".
# If the mouse steps outside the cupboard area, the cat will attack, and
# the cheese hunt is over. In that case, the program ends, keep the last known position of the mouse,
# before it steps outside the cupboard area and the following message is
# printed on the Console: "No more cheese for tonight!"
# Possible characters in the matrix are:
#     • M - represents the mouse's position.
#     • C – represents a piece of cheese.
#     • * – represents an empty position, nothing happens if the mouse steps on it.
#     • @ – represents a wall in the cupboard, cannot step on or go through it.
#     • T – represents a trap.
# The mouse starts from the M - position.
#     • If the mouse steps on the C – position, it eats the cheese from the field, and
# the position is marked with "*".
#     ◦ If this is the last cheese in the cupboard area, the mouse goes to sleep.
# Remember that this will be the last known position of the mouse. The program ends and the following message is printed on the Console: "Happy mouse! All the cheese is eaten, good night!"
#     • If the mouse steps into a trap (T -position), it will be trapped.
# Remember that this will be the last known position of the mouse.
# In that case, the program ends, and the following message is printed on the Console: "Mouse is trapped!"
#     • If the given direction leads the mouse towards the @ - position, this is a wall in
# the cupboard area. Do not make the move and skip the command.
#     • If the "danger" command is received before the mouse manages to eat all the cheese,
# the mouse disappears. Remember that this will be the last known position of the mouse and
# you will need it for the final state of the matrix. In that case, the program ends, and
# the following message is printed on the Console: "Mouse will come back later!"
# In the end, print the final state of the matrix (cupboard area) with
# the last known position of the mouse in it. Each row is on a new line.
# Input
#     • On the first line you will get the number of rows and columns of the matrix,
# separated by a comma.
#     • On the next N lines, you will receive strings, representing each row of the matrix.
#     • On each of the following lines, until the command "danger" appears as an input string,
# you will receive the possible directions for the mouse to move - "up", "down", "right", and "left".
#     • "danger" command – The mouse spots danger and disappears… for now!
# Output
#     • On the first line:
#         ◦ If the mouse steps outside the cupboard
# "No more cheese for tonight!"
#
#         ◦ If the mouse manages to eat all the cheese
# "Happy mouse! All the cheese is eaten, good night!"
#
#         ◦ If the mouse steps into a trap (T -position)
# "Mouse is trapped!"
#
#         ◦ If the "danger" command is received before the mouse manages to eat all the cheese –
# "Mouse will come back later!"
#
#     • On the next lines, print the final state of the matrix with
# the last known position of the mouse in it.
# Each row - on a new line, each row position with NO separator.
# Constraints
#     • There will always be at least one trap in the cupboard.
#     • There will always be some cheese in the cupboard.
#     • There will always be а "danger" command in the end, but it is not
# necessary to reach it. The program may end earlier.
#     • Each row of the matrix will have the same length.

# Input:
#     6,3
#     @CC
#     @TC
#     @C*
#     @M*
#     @**
#     @**
#     left
#     up
#     left
#     right
#     up
#     up
#     left
#     left
#     danger
# Output:
#     Happy mouse! All the cheese is eaten, good night!
#     @M*
#     @T*
#     @**
#     @**
#     @**
#     @**