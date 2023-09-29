# def even_odd(*args):
#     command = args[-1]
#     if command == "even":
#         return [x for x in args[:-1] if x % 2 == 0]
#     else:
#         return [x for x in args[:-1] if x % 2 != 0]
#
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))

def even_odd(*args):
    command = args[-1]
    if command == "even":
        return list(filter(lambda x: x % 2 == 0, args[:-1]))
    else:
        return list(filter(lambda x: x % 2 != 0, args[:-1]))

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))


# Create a function called even_odd() that can receive a different quantity of numbers
# and a command at the end.
# The command can be "even" or "odd". Filter the numbers depending on the command and return them in a list.
# Submit only the function in the judge system.
#
# Input:
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# Output:
# [2, 4, 6]
#
# Input:
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
# Output:
# [1, 3, 5, 7, 9]