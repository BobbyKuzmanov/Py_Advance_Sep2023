txt = tuple(input())
unique_symbols = sorted(set(txt))
for el in unique_symbols:
    print(f"{el}: {txt.count(el)} time/s")

#       #Solution 2:
# text = input()
# symbols = set(text)
# for symbol in sorted(symbols):
#     print(f"{symbol}: {text.count(symbol)} time/s")
#
#       #Solution 3:
# text = input()
# symbols = {}
# for char in text:
#     if char not in symbols:
#         symbols[char] = 0
#     symbols[char] += 1
#
# for key, value in sorted(symbols.items()):
#     print(f"{key}: {value} time/s")

# Write a program that reads a text from the console and counts the occurrences of each character in it.
# Print the results in alphabetical (lexicographical) order.
#
# # Input:
#     SoftUni rocks
# # Output:
#      : 1 time/s
#     S: 1 time/s
#     U: 1 time/s
#     c: 1 time/s
#     f: 1 time/s
#     i: 1 time/s
#     k: 1 time/s
#     n: 1 time/s
#     o: 2 time/s
#     r: 1 time/s
#     s: 1 time/s
#     t: 1 time/s
