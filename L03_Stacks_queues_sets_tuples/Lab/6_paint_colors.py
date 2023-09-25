from collections import deque

color_string = deque(input().split())
main_colors = ["red", "yellow", "blue"]
secondary_colors = {"orange": ["red", "yellow"], "purple": ["red", "blue"],
                    "green": ["yellow", "blue"] }

collected_colors = []

while color_string:
    first_str =  color_string.popleft()
    last_str = color_string.pop() if color_string else ""
    if first_str + last_str in main_colors or first_str + last_str in secondary_colors:
        collected_colors.append(first_str + last_str)
    elif  last_str + first_str in main_colors or last_str + first_str in secondary_colors:
        collected_colors.append(last_str + first_str)
    else:
        if len(first_str) > 1:
            color_string.insert(len(color_string) // 2, first_str[:-1])
        if len(last_str) > 1:
            color_string.insert(len(color_string) // 2, last_str[:-1])

for color in collected_colors:
    if color in secondary_colors:
        for el in secondary_colors[color]:
            if el not in collected_colors:
                collected_colors.remove(color)
                break

print(collected_colors)

# Write a program that finds colors in a string. You will be given a string on a single line containing
# substrings (separated by a single space) from which you will be able to form the following colors:
# Main colors: "red", "yellow", "blue"
# Secondary colors: "orange", "purple", "green"
# To form a color, you should concatenate the first and the last substrings and check if you can get any of the above
# colors' names. If there is only one substring left, you should use it to do the same check.
# You can only keep a secondary color if the two main colors needed for
# its creation could be formed from the given substrings:
#     • orange = red + yellow
#     • purple = red + blue
#     • green = yellow + blue
# Note: You could find some of the main colors needed to keep a secondary color after it is found.
# When you form a color, remove both substrings. Otherwise, you should remove the last character of each substring and
# return them in the middle of the original string. If the string contains an odd number of substrings,
# you should put the substrings one position ahead.
# For example, if you are given the string "re yellow bye" you could not form a color with the substring "re" and "bye",
# so you should remove the last character and return them in the middle of the string: "r by yellow".
# In the end, print out the list with colors in the order in which they are found.
# Input
#     • Single line string
# Output
#     • The list with the collected colors
# Constraints
#     • You will not receive an empty string
#     • Please consider only the colors mentioned above
#     • There won't be any cases with repeating colors
#
# Input:
#     d yel blu e low redd
# Output:
#     ['yellow', 'blue', 'red']
#
# Input:
#     r ue nge ora bl ed
# Output:
#     ['red', 'blue']
#
# Input:
#     re ple blu pop e pur d
# Output:
#     ['red', 'purple', 'blue']
