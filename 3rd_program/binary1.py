class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Binary Tree
root = Node(input("Enter root: "))
root.left = Node(input("Enter left child: "))
root.right = Node(input("Enter right child: "))

print("Inorder:", end=" ")
inorder(root)

print("\nPreorder:", end=" ")
preorder(root)

print("\nPostorder:", end=" ")
postorder(root)


# Expression Tree
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+ - * /): ")

expr = Node(op)
expr.left = Node(a)
expr.right = Node(b)

print("Expression:", a, op, b)

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    result = a / b

print("Result:", result)