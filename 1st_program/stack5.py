orders = []

while True:
    print("\n1. Add Order  2. Cancel Last Order  3. Orders  4. Exit")
    ch = input("Choice: ")

    if ch == '1':
        order = input("Enter order: ")
        orders.append(order)
        print("Order added")

    elif ch == '2':
        if orders:
            print("Cancelled:", orders.pop())
        else:
            print("No orders")

    elif ch == '3':
        print("Orders:", orders)

    elif ch == '4':
        break