input_string = input()

stack = []
for char in input_string:
    stack.append(char)

reversed_string = ''
while stack:
    reversed_string += stack.pop()

print(reversed_string)


# Write a program that:
#
# · Reads an input string
#
# · Reverses it using a stack
#
# · Prints the result back on the console
#
# Examples
#
# Input
#   I Love Python
#
# Output
#   nohtyP evoL I
