field_size = int(input())
squirrel_directions = input().split(', ')

hazelnuts_collected = 0
s_row = 0
s_col = 0
is_game_over = False

field_matrix = []
for row in range(field_size):
    field_matrix.append(list(input()))
    for col in range(field_size):
        if field_matrix[row][col] == 's':
            s_row = row
            s_col = col

for direction in squirrel_directions:
    field_matrix[s_row][s_col] = '*'

    if direction == 'up':
        s_row -= 1
    elif direction == 'down':
        s_row += 1
    elif direction == 'left':
        s_col -= 1
    elif direction == 'right':
        s_col += 1

    if not (0 <= s_row < field_size and 0 <= s_col < field_size):
        print("The squirrel is out of the field.")
        is_game_over = True
        break
    if field_matrix[s_row][s_col] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        is_game_over = True

    if field_matrix[s_row][s_col] == 'h':
        hazelnuts_collected += 1
        if hazelnuts_collected == 3:
            is_game_over  = True
            print("Good job! You have collected all hazelnuts!")
            break

if hazelnuts_collected < 3 and not is_game_over:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts_collected}")


# The game starts with 0 collected hazelnuts. Your goal is to collect 3 of them.
# You get as input the size of the field, which will be always a square shape. After that, you will receive the
# directions in which the squirrel can move – "left", "right", "down", and "up" in a sequence,
# each value separated by a comma and a space (", "). On the next rows, you will receive the field.
# Possible characters in the field:
#     • s - represents the squirrel's position.
#     • h – represents a hazelnut.
#     • * – the asterisk represents an empty position.
#     • t – represents a trap.
# The squirrel starts from the s - s-position.
#     • If the squirrel steps on a hazelnut, you have to increase them by 1.
# The position should be marked with an asterisk (*).
#     ◦ If the squirrel collects all 3 hazelnuts, the game ends.
#     • Asterisk (*) does nothing, so nothing happens if the squirrel steps on it.
#     • If it steps on a trap, the game ends.
#     • If the squirrel moves out of the field, the game ends.
# After all commands you will have 4 possible results:
#     • You win if the squirrel collects 3 of the hazelnuts.
#     • The squirrel collects less than 3 hazelnuts.
#     • The squirrel steps on a trap.
#     • The squirrel moves out of the field.
# Input
#     • On the first line, you will receive the length of the field – an integer number in the range [3, 5].
#     • On the second line, you will receive the commands to move the squirrel – an array of strings separated by ", ".
#     • In the next N lines, you will receive the values for every row.
# Output
#     • On the first line:
#         ◦ If the squirrel goes out of the field - "The squirrel is out of the field.".
#         ◦ If the squirrel steps on a trap - "Unfortunately, the squirrel stepped on a trap...".
#         ◦ If the squirrel hasn’t collected all the hazelnuts - "There are more hazelnuts to collect.".
#         ◦ If the squirrel has collected all hazelnuts - "Good job! You have collected all hazelnuts!".
#     • On the second line, print the number of collected hazelnuts - "Hazelnuts collected: {hazelnutsCount}"
# Constraints
#     • The size of the field will be between [3,5].
#
# Input:
#     5
#     left, left, up, right, up, up
#     **h**
#     t****
#     *h***
#     *h*s*
#     *****
# Output:
#     Good job! You have collected all hazelnuts!
#     Hazelnuts collected: 3
#
# Input:
#     4
#     down, down, right, right
#     *s*h
#     ***h
#     ***t
#     h***
# Output:
#     Unfortunately, the squirrel stepped on a trap...
#     Hazelnuts collected: 0