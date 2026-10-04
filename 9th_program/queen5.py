n = int(input("Enter number of satellites: "))

channel = [-1] * n

def safe(satellite, ch):
    for i in range(satellite):
        if channel[i] == ch:
            return False
    return True

def solve(satellite):
    if satellite == n:
        print("\nSatellite Channels:")
        for i in range(n):
            print("Satellite", i + 1, "-> Channel", channel[i] + 1)
        return True

    for ch in range(n):
        if safe(satellite, ch):
            channel[satellite] = ch

            if solve(satellite + 1):
                return True

            channel[satellite] = -1

    return False

if not solve(0):
    print("No valid assignment")