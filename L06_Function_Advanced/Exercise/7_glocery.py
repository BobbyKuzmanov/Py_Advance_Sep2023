def grocery_store(**kwargs):
    receipt = dict(sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0])))
    result = []
    for product, quantity in receipt.items():
        result.append(f'{product}: {quantity}')

    return '\n'.join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
    ))

# def grocery_store(**kwargs):
#     # Create a list of tuples from the keyword arguments
#     products = [(name, quantity) for name, quantity in kwargs.items()]
#
#     # Sort the list of tuples by quantity in descending order,
#     # then by name's length in descending order,
#     # and finally by name in ascending order
#     products.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))
#
#     # Create a string representation of the sorted receipt
#     receipt = '\n'.join([f'{name}: {quantity}' for name, quantity in products])
#
#     return receipt

# Create a function called grocery_store() that receives a different number of key-value pairs.
# The key will be the product's name and the value - its quantity.
# You should return a sorted receipt for all products.
# They should be sorted by their quantity in descending order.
# If there are two or more products with the same quantity, sort them by their name's length in descending order. '
# If there are two or more products with the same name's length, sort them by their name in
# ascending order (alphabetically).
# In the end, return a string in the following format:
# "{product_name1}: {product_quantity1}
# {product_name2}: {product_quantity2}
# …
# {product_nameN}: {product_quantityN}"
#
# Input:
# print(grocery_store(
#     bread=5,
#     pasta=12,
#     eggs=12,
# ))
# Output:
# pasta: 12
# eggs: 12
# bread: 5
#
# Input:
# print(grocery_store(
#     bread=2,
#     pasta=2,
#     eggs=20,
#     carrot=1,
# ))
# Output:
# eggs: 20
# bread: 2
# pasta: 2
# carrot: 1
