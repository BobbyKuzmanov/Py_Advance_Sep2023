number = int(input())
stack = []

for _ in range(number):
    query = input().split()
    if query[0] == '1':
        stack.append(int(query[1]))
        continue

    if query[0] == '2':
        if stack:
            stack.pop()
        continue

    if query[0] == '3':
        if stack:
            print(max(stack))
        continue

    if query[0] == '4':
        if stack:
            print(min(stack))


reversed_stack = []
while stack:
    reversed_stack.append(str(stack.pop()))

print(', '.join(reversed_stack))


# You have an empty stack. You will receive an integer – N.
# On the following N lines, you will receive queries. Each query is one of these four types:
#     • '1 {number}' – push the number (integer) into the stack
#     • '2' – delete the number at the top of the stack
#     • '3' – print the maximum number in the stack
#     • '4' – print the minimum number in the stack
# It is guaranteed that each query is valid.
# After you go through all the queries, print the stack from top to bottom in the following format:
# "{n}, {n1}, {n2}, ... {nn}"

# Input:
# 9
# 1 97
# 2
# 1 20
# 2
# 1 26
# 1 20
# 3
# 1 91
# 4

# Output:
# 26
# 20
# 91, 20, 26