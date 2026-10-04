history = []

while True:
    print("\n1. Visit Page  2. Back  3. History  4. Exit")
    ch = input("Choice: ")

    if ch == '1':
        page = input("Enter website: ")
        history.append(page)
        print("Visited:", page)

    elif ch == '2':
        if history:
            print("Going back from:", history.pop())
        else:
            print("No previous page")

    elif ch == '3':
        print("History:", history)

    elif ch == '4':
        break