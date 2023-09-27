def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

def operate(operator, *args):
    if operator == "+":
        return sum(args)
    elif operator == "-":
        return args[0] - sum(args[1:])
    elif operator == "*":
        return multiply(*args)
    elif operator == "/":
        return args[0] / multiply(*args[1:])

# print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))


# Write a function called operate that receives an operator ("+", "-", "*" or "/") as а first argument and
# multiple numbers (integers) as additional arguments (*args).
# The function should return the result of the operator applied to all the numbers.
# For more clarification, see the examples below.
# Submit only your function in the Judge system.
# Note: Be careful when you have if multiplication and division:
#
# # Input
#  print(operate("+", 1, 2, 3))
#
# # Output
#   6
#
# Input:
#   print(operate("*", 3, 4))
# Output:
#   12