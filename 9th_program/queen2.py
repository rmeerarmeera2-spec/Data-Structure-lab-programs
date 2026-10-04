n = int(input("Enter number of classes: "))

schedule = [-1] * n

def safe(cls, period):
    for i in range(cls):
        if schedule[i] == period:
            return False
    return True

def solve(cls):
    if cls == n:
        print("\nClass Schedule:")
        for i in range(n):
            print("Class", i + 1, "-> Period", schedule[i] + 1)
        return True

    for period in range(n):
        if safe(cls, period):
            schedule[cls] = period

            if solve(cls + 1):
                return True

            schedule[cls] = -1

    return False

if not solve(0):
    print("No valid schedule found")