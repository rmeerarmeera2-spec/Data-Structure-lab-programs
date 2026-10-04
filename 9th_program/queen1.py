n = int(input("Enter number of queens: "))

board = [-1] * n
count = 0

def safe(row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(row):
    global count

    if row == n:
        count += 1
        print("\nSolution", count)

        for i in range(n):
            for j in range(n):
                if board[i] == j:
                    print("Q", end=" ")
                else:
                    print("-", end=" ")
            print()
        return

    for col in range(n):
        if safe(row, col):
            board[row] = col
            solve(row + 1)
            board[row] = -1

solve(0)

print("\nTotal Solutions:", count)