screens = ["Home"]

while True:
    print("\nCurrent Screen:", screens[-1])
    print("1. Open Screen  2. Back  3. Exit")
    ch = input("Choice: ")

    if ch == '1':
        screen = input("Enter screen name: ")
        screens.append(screen)
        print("Opened:", screen)

    elif ch == '2':
        if len(screens) > 1:
            print("Back from:", screens.pop())
        else:
            print("Already at Home")

    elif ch == '3':
        break