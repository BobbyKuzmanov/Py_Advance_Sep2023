n = int(input())
unique_elements = set()
for _ in range(n):
    elements = input().split()
    for element in elements:
        unique_elements.add(element)

print(*unique_elements, sep='\n')

# Write a program that keeps all the unique chemical elements.
# On the first line, you will be given a number n - the count of input lines that you will receive.
# On the following n lines, you will be receiving chemical compounds separated by a single space.
# Your task is to print all the unique ones on separate lines (the order does not matter):
#
# Input:
#     4
#     Ce O
#     Mo O Ce
#     Ee
#     Mo
# Output:
#     Ce
#     Ee
#     Mo
#     O