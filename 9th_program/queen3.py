n = int(input("Enter number of cars: "))

slot = [-1] * n

def safe(car, s):
    for i in range(car):
        if slot[i] == s:
            return False
    return True

def solve(car):
    if car == n:
        print("\nParking Allocation:")
        for i in range(n):
            print("Car", i + 1, "-> Slot", slot[i] + 1)
        return True

    for s in range(n):
        if safe(car, s):
            slot[car] = s

            if solve(car + 1):
                return True

            slot[car] = -1

    return False

if not solve(0):
    print("No valid allocation")