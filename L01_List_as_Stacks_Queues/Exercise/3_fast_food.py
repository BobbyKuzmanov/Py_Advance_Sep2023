quantity_food = int(input())
orders = [int(x) for x in input().split()]
print(max(orders))

while orders:
    if quantity_food >= orders[0]:
        quantity_food -= orders[0]
        orders.pop(0)
    else:
        break

if orders:
    print('Orders left:', end=' ')
    print(*orders, sep=' ')

else:
    print('Orders complete')

# Write a program that checks if you have enough food to serve lunch to all your customers.
# You also want to know who the client with the biggest order for that day is.
# First, you will be given the quantity of food you have for the day (an integer number).
# Next, you will be given a sequence of integers (separated by a single space),
# each representing the quantity of food in each order. Keep the orders in a queue.
# Find the biggest order and print it. Next, you will begin servicing your clients from the first one that came.
# Before each order, check if you have enough food left to complete it:
#     • If you have, remove the order from the queue and reduce the quantity of food in the restaurant.
#     • Otherwise, stop serving.
# Input
#    • On the first line, you will be given the quantity of your food - an integer in the range [0, 1000]
#    • On the second line, you will receive a sequence of integers, representing each order, separated by a single space
# Output
#    • On the first line, print the quantity of the biggest order
#    • On the second line:
#         ◦ If you succeeded in servicing all your clients, print: "Orders complete".
#         ◦ Otherwise, print: "Orders left: {order1} {order2} .... {orderN}".
# Constraints
#     • The input will always be valid
#
# Input:
#     348
#     20 54 30 16 7 9
# Output:
#     54
#     Orders complete
#
# Input:
#     499
#     57 45 62 70 33 90 88 76 100 50
# Output:
#     100
#     Orders left: 76 100 50
