class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(input("Enter Manager: "))
root.left = Node(input("Enter Employee 1: "))
root.right = Node(input("Enter Employee 2: "))

print("\nOrganization:")
print("Manager:", root.data)
print("Employee 1:", root.left.data)
print("Employee 2:", root.right.data)