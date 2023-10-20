from collections import deque

programmers_time = deque([int(x) for x in input().split()])
num_of_tasks = [int(x) for x in input().split()]

duck_types = {
    'Darth Vader Ducky': 0,
    'Thor Ducky':0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0
}

while programmers_time and num_of_tasks:
    current_time = programmers_time.popleft()
    current_task = num_of_tasks.pop()
    total_time = current_time * current_task

    if 0 < total_time <= 60:
        duck_types['Darth Vader Ducky'] += 1
    elif 60 < total_time <= 120:
        duck_types['Thor Ducky'] += 1
    elif 120 < total_time <= 180:
        duck_types['Big Blue Rubber Ducky'] += 1
    elif 180 < total_time <= 240:
        duck_types['Small Yellow Rubber Ducky'] += 1
    else:
        programmers_time.append(current_time)
        num_of_tasks.append(current_task - 2)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded: ")

for key, value in duck_types.items():
    print(f"{key}: {str(value)}")


# You will be given two sequences of integers. The first one represents the time it takes a programmer
# to complete a single task. The second one represents the number of tasks you’ve given to your programmers.
# Your task is to count how many rubber ducks of each type you’ve given to your programmers.
# While you have values in the sequences, you need to start from the first value of the programmers
# time's sequence and multiply them by the last value of the tasks' sequence:
#     • If the calculated time is between any of the time ranges below,
# you give the corresponding ducky and remove the programmer time's value and the tasks' value.
#     • If the calculated time goes above the highest range, decrease the number of the tasks value by 2.
# Then, move the programmer time's value to the end of its sequence, and continue with the next operation.
# Rubber Ducky type         Time needed to earn it
#  Darth Vader Ducky            0 - 60
#  Thor Ducky                   61 – 120
#  Big Blue Rubber Ducky        121 - 180
#  Small Yellow Rubber Ducky    181 - 240

# Your task is considered done when the sequences are empty.
# Input
#     • The first line will represent each programmer’s time to complete a single task – integers,
# separated by a single space.
#     • The second line will represent the number of tasks that should be completed – integers,
# separated by a single space.
# Output
#     • On the first line, you output:
#         ◦ "Congratulations, all tasks have been completed! Rubber ducks rewarded:"
#     • On the next 4 lines, you output the type and number of ducks given, ordered like in the table:
#         ◦ "Darth Vader Ducky: {count}
# Thor Ducky: {count}
# Big Blue Rubber Ducky: {count}
# Small Yellow Rubber Ducky: {count}"
# Constraints
#     • All the given numbers will be valid integers in the range [1, 1000].
#     • There will be no negative inputs.
#     • The number of values in both sequences will always be equal.
#
# Input:
#     10 15 12 18 22 6
#     12 16 5 6 9 1
# Output:
#     Congratulations, all tasks have been completed! Rubber ducks rewarded:
#     Darth Vader Ducky: 1
#     Thor Ducky: 3
#     Big Blue Rubber Ducky: 1
#     Small Yellow Rubber Ducky: 1
#
# Input:
#     2 55 17 31 23
#     7 5 17 4 27
# Output:
#     Congratulations, all tasks have been completed! Rubber ducks rewarded:
#     Darth Vader Ducky: 1
#     Thor Ducky: 0
#     Big Blue Rubber Ducky: 2
#     Small Yellow Rubber Ducky: 2
