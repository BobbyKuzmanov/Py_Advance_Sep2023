import os

while True:
    command, *args = input().split('-') # Add - some_file.txt - some text

    if command == "Create":
        file = open(f'files/{args[0]}',  'w')
        file.close()

    elif command == "Add":
        with open(f'files/{args[0]}', 'a') as file:
            file.write(f'{args[1]}\n')

    elif command == "Replace":
        try:
            with open(f'files/{args[0]}', 'r') as file:
                text = file.readlines()
            for i in range(len(text)):
                text[i] = text[i].replace(args[1], args[2])

            with open(f'files/{args[0]}', 'w') as file:
                file.write(' '.join(text))
        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        try:
            os.remove(f'file/{args[0]}')
        except FileNotFoundError:
            print("An error occurred")

    if command == "End":
        break