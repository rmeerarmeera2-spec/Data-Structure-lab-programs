orders = []

n = int(input("Enter number of orders: "))

for i in range(n):
    order = input("Enter food order: ")
    orders.append(order)

print("Order Queue:", orders)

print("Preparing:", orders.pop(0))

print("Pending Orders:", orders)