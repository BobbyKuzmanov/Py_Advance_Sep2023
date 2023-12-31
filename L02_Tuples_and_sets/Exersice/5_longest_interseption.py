n = int(input())

longest_intersection = set()

for _ in range(n):
    first_range, second_range= input().split('-')
    first_start, first_end = [int(x) for x in first_range.split(',')]
    second_start, second_end = [int(x) for x in second_range.split(',')]

    first_set = set(range(first_start, first_end+1))
    second_set = set(range(second_start, second_end+1))

    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")

# Write a program that finds the longest intersection. You will be given a number N.
# On each of the next N lines you will be given two ranges in the format:
# "{first_start},{first_end}-{second_start},{second_end}".
# You should find the intersection of these two ranges. The start and end numbers in the ranges are inclusive.
# Finally, you should find the longest intersection of all N intersections,
# print the numbers that are included and its length in the format:
#     "Longest intersection is [{longest_intersection_numbers} with length {length_longest_intersection}"
# Note: in each range, there will always be an intersection. If there are two equal intersections, print the first one.
#
# Input:
# 3
# 0,3-1,2
# 2,10-3,5
# 6,15-3,10
# Output:
# Longest intersection is [6, 7, 8, 9, 10] with length 5