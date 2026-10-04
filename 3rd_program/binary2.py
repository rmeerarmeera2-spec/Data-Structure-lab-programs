class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(input("Enter main folder: "))
root.left = Node(input("Enter left folder: "))
root.right = Node(input("Enter right folder: "))

print("Folder Structure:")
print(root.data)
print("Left:", root.left.data)
print("Right:", root.right.data)