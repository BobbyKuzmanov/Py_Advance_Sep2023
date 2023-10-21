from collections import deque

textiles = deque(map(int, input().split()))
medicaments = list(map(int, input().split()))

items = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while True:
    if not textiles and not medicaments:
        print("Textiles and medicaments are both empty.")
        break
    if not textiles:
        print("Textiles are empty.")
        break
    if not medicaments:
        print("Medicaments are empty.")
        break
    first_textile = textiles.popleft()
    last_medicament = medicaments.pop()
    summed_items = first_textile + last_medicament
    if summed_items == 30:
        items["Patch"] += 1
    elif summed_items == 40:
        items["Bandage"] += 1
    elif summed_items == 100:
        items["MedKit"] += 1
    elif summed_items > 100:
        items["MedKit"] += 1
        summed_items -= 100
        medicaments[-1] += summed_items
    else:
        last_medicament += 10
        medicaments.append(last_medicament)

sorted_items = sorted(items.items(), key=lambda x: (-x[1], x[0]))
for item in sorted_items:
    if int(item[1]) > 0:
        print(f"{item[0]} - {item[1]}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicaments))}")
if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")



# On the first line, you will be given a sequence representing textiles.
# On the second line, you will be given another sequence, which represents medicaments.
# While both collections contain any elements, you will have to combine elements from the collections
# in order to create healing items.
# You should start by getting the first value of textile and the last value of medicaments:
#     • If their sum is equal to any of the items in the table below create that item and remove both values.
#     • Otherwise, check if the sum is bigger than the value of the MedKit, create the MedKit,
# remove both values, and add the remaining resources(of the sum) to the next value in the medicament
# collection (Take the element from the collection, add the remaining sum to it, and put the element back to its place).
#     • If you can’t create anything, remove the textile value, add 10 to the medicament value,
# and return the medicament back to its place, into its collection.
# You need to stop creating healing items when either the textile or the medicaments are exhausted.
#
# Healing item        Resources needed
#   Patch               30
#   Bandage             40
#   MedKit              100
#
# In the end, you should print on the console message for the sequence that has ended, then the created items,
# and in the end the remaining items (if any).
# Input
#     • On the first line, you will receive a sequence of integers representing the textiles,
# separated by a single space (" ").
#     • On the second line, you will receive a sequence of integers representing the medicaments,
# separated by a single space (" ").
# Output
#     • On the first line print which one of the collections is over:
#         ◦ If the textile is over print: "Textiles are empty."
#         ◦ If the medicaments are over print: "Medicaments are empty."
#         ◦ If both are empty print: "Textiles and medicaments are both empty."
#     • On the next n lines print only the created items (if any) ordered by the amount created descending,
# then by name alphabetically:
# "{item name} - {amount created}
#   {item name} - {amount created}
# …
# "
# Hint: Do not print items, which are not created.
#     • On the last line print the remaining items(if any):
#     • If there are any medicaments left:
#  "Medicaments left: …{medicament2}, {medicament1}"
#     • If there are any textiles left:
# "Textiles left: {textile1}, {textile2}…"
# Constraints
#     • All the numbers will be in the range [0…1000].
#     • All the inputs will be valid.
#
# Input:
#     20 10 40 70 20
#     10 50 10 30 20 80
# Output:
#     Textiles are empty.
#     MedKit - 2
#     Bandage - 1
#     Patch - 1
#     Medicaments left: 50, 10
#
# Input:
#     30 30 10 80 60
#     40 20 30 10 70
# Output:
#     Textiles and medicaments are both empty.
#     MedKit - 3
#     Bandage - 2