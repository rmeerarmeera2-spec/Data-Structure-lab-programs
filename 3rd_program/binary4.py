class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(input("Enter Department: "))
root.left = Node(input("Enter Staff 1: "))
root.right = Node(input("Enter Staff 2: "))

print("\nDepartment:")
print("Department:", root.data)
print("Staff 1:", root.left.data)
print("Staff 2:", root.right.data)