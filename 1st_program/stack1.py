stack = []

def push():
    x = input("Enter value: ")
    stack.append(x)
    print("Pushed:", x)

def pop():
    if stack:
        print("Popped:", stack.pop())
    else:
        print("Stack Empty")

def peek():
    if stack:
        print("Top:", stack[-1])
    else:
        print("Stack Empty")

def evaluate():
    exp = input("Enter expression: ")
    try:
        print("Result:", eval(exp))
    except:
        print("Invalid Expression")

while True:
    print("\n1.Push  2.Pop  3.Peek  4.Display  5.Evaluate  6.Exit")
    ch = input("Enter choice: ")

    if ch == '1':
        push()
    elif ch == '2':
        pop()
    elif ch == '3':
        peek()
    elif ch == '4':
        print("Stack:", stack)
    elif ch == '5':
        evaluate()
    elif ch == '6':
        break
    else:
        print("Invalid Choice")