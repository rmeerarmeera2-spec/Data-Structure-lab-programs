n = int(input("Enter number of CCTV cameras: "))

camera = [-1] * n

def safe(row, col):
    for i in range(row):
        if camera[i] == col:
            return False

        if abs(camera[i] - col) == abs(i - row):
            return False

    return True

def solve(row):
    if row == n:
        print("\nCCTV Placement:")
        for i in range(n):
            for j in range(n):
                if camera[i] == j:
                    print("C", end=" ")
                else:
                    print("-", end=" ")
            print()
        return True

    for col in range(n):
        if safe(row, col):
            camera[row] = col

            if solve(row + 1):
                return True

            camera[row] = -1

    return False

if not solve(0):
    print("No valid placement")