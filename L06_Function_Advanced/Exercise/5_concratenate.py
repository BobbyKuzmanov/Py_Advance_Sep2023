def concatenate(*args, **kwargs):
    result = ""
    for string in args:
        result += string
    for key, value in kwargs.items():
        if  key in result:
            result = result.replace(key, value)
    return result

print(concatenate("Soft", "UNI", "Is", "Grate", "!",
                   UNI="Uni", Grate="Great"))
print()
print(concatenate("I", " ", "Love", " ", "Cythons",
                  C="P", s="", java='Java'))

# def concatenate(*args, **kwargs):
#     result = ''.join(args)
#     for key, value in kwargs.items():
#         result = result.replace(key, value)
#     return result

# Write a concatenate() function that receives some strings as arguments and
# some named arguments the key will be a string, and the value will be another string.
# First, you should concatenate all arguments successively. Next, take each key successively,
# and if it is present in the resulting string, change all matching parts with the key's value.'
# In the end, return the final string.
#  See the examples for more clarification.
#
# Input:
# print(concatenate("Soft", "UNI", "Is", "Grate", "!",
#                   UNI="Uni", Grate="Great"))
# Output:
# SoftUniIsGreat!
#
# Input:
# print(concatenate("I", " ", "Love", " ", "Cythons",
#                   C="P", s="", java='Java'))
# Output:
# I Love Python