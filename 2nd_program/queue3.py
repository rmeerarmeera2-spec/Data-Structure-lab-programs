queue = []

n = int(input("Enter number of customers: "))

for i in range(n):
    name = input("Enter customer name: ")
    queue.append(name)

print("Customer Queue:", queue)

print("Serving:", queue.pop(0))

print("Remaining Queue:", queue)