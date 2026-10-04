class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(input("Enter Parent: "))
root.left = Node(input("Enter Child 1: "))
root.right = Node(input("Enter Child 2: "))

print("\nFamily Tree:")
print("Parent:", root.data)
print("Child 1:", root.left.data)
print("Child 2:", root.right.data)