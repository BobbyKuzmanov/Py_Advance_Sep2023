def recursive_power( number, power):
    if power == 1:
        return number
    return number * recursive_power(number, power - 1)

print(recursive_power(2, 10))

# Create a recursive function called recursive_power() which should receive a number and a power. Using recursion,
# return the result of number ** power. Submit only the function in the judge system.
#
# # Input
# print(recursive_power(2, 10))
# # Output
# 1024
#
# Input:
# print(recursive_power(10, 100))
# # Output
# 100000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000