actions = []

while True:
    print("\n1. Type  2. Undo  3. Show  4. Exit")
    ch = input("Choice: ")

    if ch == '1':
        text = input("Enter text: ")
        actions.append(text)
        print("Text added")

    elif ch == '2':
        if actions:
            print("Undo:", actions.pop())
        else:
            print("Nothing to undo")

    elif ch == '3':
        print("Current Text:", actions)

    elif ch == '4':
        break