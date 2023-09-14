from collections import deque

# Initialize the queue to store people waiting for water
queue = deque()

# Read the starting quantity of water
starting_water = int(input())

# Read the initial commands and process them
while True:
    command = input()
    if command == "Start":
        break
    queue.append(command)

# Process commands until "End" is received
while True:
    command = input()
    if command == "End":
        break
    if command.startswith("refill"):
        # Extract the liters to refill and add it to the starting water
        refill_liters = int(command.split()[1])
        starting_water += refill_liters
    else:
        # Extract the liters requested by the current person
        requested_liters = int(command)
        if starting_water >= requested_liters:
            # If there is enough water, provide water to the person
            print(f"{queue[0]} got water")
            starting_water -= requested_liters
            queue.popleft()
        else:
            # If there isn't enough water, the person must wait
            print(f"{queue[0]} must wait")
            queue.popleft()

# Print the remaining water
print(f"{starting_water} liters left")

# Write a program that keeps track of people getting water from a dispenser and the amount of water left at the end.
# On the first line, you will receive the starting quantity of water (integer) in a dispenser.
# Then, on the following lines, you will be given the names of some people who want to get water
# (each on a separate line) until you receive the command "Start".
# Add those people to a queue. Finally, you will receive some commands until the command "End":
#     • "{liters}" - litters (integer) that the current person in the queue wants to get. Check if there is enough water in the dispenser for that person.
#         ◦ If there is enough water, print "{person_name} got water" and remove him/her from the queue.
#         ◦ Otherwise, print "{person_name} must wait" and remove the person from the queue without reducing the water in the dispenser.
#     • "refill {liters}" - add the given litters in the dispenser.
# In the end, print how many liters of water have left in the format: "{left_liters} liters left".

# Input:
#     2
#     Peter
#     Amy
#     Start
#     2
#     refill 1
#     1
#     End
#
# Output:
#     Peter got water
#     Amy got water
#     0 liters left
