def nums_sums(*args):
    neg_sum = 0
    pos_sum = 0
    for num in args:
        if num  > 0:
            pos_sum += num
        else:
            neg_sum += num

    return neg_sum, pos_sum


nums = [int(x) for x in input().split()]
# print and unpack the list
print(nums_sums(*nums)[0])
print(nums_sums(*nums)[1])
if abs(nums_sums(*nums)[0]) > nums_sums(*nums)[1]:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")


# sequence_nums = [int(x) for x in input().split()]
#
# negative_nums = []
# positive_nums = []
# negative_sum = 0
# positive_sum = 0
#
# for num in sequence_nums:
#     if num < 0:
#         negative_nums.append(num)
#     else:
#         positive_nums.append(num)
#
# for negative in negative_nums:
#     negative_sum += negative
# for positive in positive_nums:
#     positive_sum += positive
#
# print(negative_sum)
# print(positive_sum)
#
# if abs(negative_sum) > positive_sum:
#     print("The negatives are stronger than the positives")
# else:
#     print("The positives are stronger than the negatives")


# You will receive a sequence of numbers (integers) separated by a single space.
# Separate the negative numbers from the positive.
# Find the total sum of the negatives and positives, and print the following:
# · On the first line, print the sum of the negatives
# · On the second line, print the sum of the positives
# · On the third line:
# o If the absolute negative number is larger than the positive number: "The negatives are stronger than the positives"
# o If the positive number is larger than the absolute negative number: "The positives are stronger than the negatives"
# Note: you will not receive any zeroes in the input.
#
# Input:
# 1 2 -3 -4 65 -98 12 57 -84
# Output:
# -189
# 137
# The negatives are stronger than the positives
#
# Input:
# 1 2 3
# Output:
# 0
# 6
# The positives are stronger than the negatives