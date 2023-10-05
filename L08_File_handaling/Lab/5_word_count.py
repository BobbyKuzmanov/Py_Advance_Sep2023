import re

# open the file for searched  word and read it
with open('words.txt', 'r') as file:
    searched_word = file.read().lower().split() # convert to lowercase and split

with open('text.txt', 'r') as file:
    text = file.read().lower() # convert to lowercase

words = {}

for searched_word  in searched_word:
    regex = re.compile(rf'\b{searched_word}\b')
    result = re.findall(regex,text)
    words[searched_word] = len(result)


with open('output.txt', 'w') as file:
    for key, value in sorted(words.items(), key=lambda kvp: -kvp[1]):
        file.write(f'{key} - {value}\n')



# Write a program that reads a list of words from the file words.txt and
# finds how many times each of the words is contained in another file text.txt.
# Matching should be case-insensitive.
# The results should be written into other text files. Sort the words by frequency in descending order.
