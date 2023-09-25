# Read the initial sequences
sequence1 = set(map(int, input().split()))
sequence2 = set(map(int, input().split()))

# Read the number of commands
n = int(input())

# Process the commands
for _ in range(n):
    command = input().split()
    operation = command[0]
    numbers = set(map(int, command[2:]))

    if operation == "Add":
        if command[1] == "First":
            sequence1.update(numbers)
        elif command[1] == "Second":
            sequence2.update(numbers)
    elif operation == "Remove":
        if command[1] == "First":
            sequence1 -= numbers
        elif command[1] == "Second":
            sequence2 -= numbers
    elif operation == "Check":
        if sequence1.issubset(sequence2) or sequence2.issubset(sequence1):
            print("True")
        else:
            print("False")

# Print the final sequences
sequence1 = sorted(sequence1)
sequence2 = sorted(sequence2)
print(", ".join(map(str, sequence1)))
print(", ".join(map(str, sequence2)))


# First, you will be given two sequences of integer values on different lines.
# The values of the sequences are separated by a single space between them.
# Keep in mind that each sequence should contain only unique values.
# Next, you will receive a number - N. On the following N lines, you will receive one of the following commands:
#     • "Add First {numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers.
#     • "Add Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers.
#     • "Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
#     • "Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
#     • "Check Subset" - check if any of the given sequences are a subset of the other. If it is, print "True".
# Otherwise, print "False".In the end, print the final sequences, separated by a comma and a space ", ".
# The values in each sequence should be sorted in ascending order.
#
# Input:
#     1 2 3 4 5
#     1 2 3
#     3
#     Add First 5 6
#     Remove Second 8 9 11
#     Check Subset
# Output:
#     True
#     1, 2, 3, 4, 5, 6
#     1, 2, 3
