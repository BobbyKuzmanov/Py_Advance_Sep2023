nums = input().split()
nums_dict = {}

for num in nums:
    if num not in nums_dict:
        nums_dict[num] = 0
    nums_dict[num] += 1

for num, count in nums_dict.items():
    print(f"{int(num):.1f} - {count} times")

# You will be given numbers separated by a space.
# Write a program that prints the number of occurrences of each number in the format "{number} - {count} times".
# The number must be formatted to the first decimal point.

# Input:
#     -2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3
# Output:
#     -2.5 - 3 times
#     4.0 - 2 times
#     3.0 - 4 times
#     -5.5 - 1 times

# Input:
# 2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3
# Output:
# 2.0 - 3 times
# 4.0 - 6 times
# 5.0 - 4 times
# 3.0 - 7 times