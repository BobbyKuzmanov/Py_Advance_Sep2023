number_of_names = int(input())
names = []
# start filling the list with names
for _ in range(number_of_names):
    names.append(input())
# print the list without duplicates
for name in set(names):
    print(name)

# Write a program, which will take a list of names and print only the unique names in the list.
# The order in which we print the result does not matter.
#
# Input:
# 8
# Lee
# Joey
# Lee
# Joe
# Alan
# Alan
# Peter
# Joey
#
# Output:
# Alan
# Joey
# Lee
# Joe
# Peter