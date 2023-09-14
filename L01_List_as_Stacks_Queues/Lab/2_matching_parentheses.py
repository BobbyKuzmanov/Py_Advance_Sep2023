expression = input()
stack = []
for i in range(len(expression)):
    if expression[i] == "(":
        stack.append(i)
    elif expression[i] == ")":
        start_index = stack.pop()
        print(expression[start_index:i + 1])

# You are given an algebraic expression with parentheses.
# Scan through the string and extract each set of parentheses.
# Print the result back on the console.

# Hints
# Scan through the expression searching for parentheses:
#     • If you find an opening parenthesis, push the index into the stack.
#     • If you find a closing parenthesis, pop the topmost element from the stack. This is the index of the last opening parenthesis.
#     • Use the current index and the popped one to extract a set of parentheses.

# Input:
# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5
#
# Output:
# (2 + 3)
# (3 + 1)
# (2 - (2 + 3) * 4 / (3 + 1))
