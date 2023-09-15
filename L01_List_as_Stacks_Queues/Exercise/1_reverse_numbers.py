numbers = input().split()
stack = []
for i in range(len(numbers)):
    stack.append(numbers[i])

for i in range(len(stack)):
    print(stack.pop(), end=' ')


# Write a program that reads a string with N integers from the console,
# separated by a single space, and reverses them using a stack.
# Print the reversed integers on one line, separated by a single space.

# Input:
#     1 2 3 4 5

# Output:
#     5 4 3 2 1

