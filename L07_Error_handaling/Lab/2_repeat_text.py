text = input()

try:
    times = int(input())
    print(text * times)

except ValueError:
    print("Variable times must be an integer")

# Write a program that receives a text on the first line and times (to repeat the text)
# that must be an integer.
# If the user passes a non-integer type for the times variable, handle the exception and print a message
# "Variable times must be an integer".
#
# Input:
#     Hello
#     Bye
# Output:
#     Variable times must be an integer
#
# Input:
#     Hello
#     2
# Output:
#     HelloHello
