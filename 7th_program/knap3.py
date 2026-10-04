items = ["Medicine", "Bandage", "Injection", "Oxygen"]
weight = [2, 1, 3, 4]
value = [50, 20, 70, 100]

capacity = int(input("Enter kit capacity: "))

dp = [0] * (capacity + 1)

for i in range(4):
    for w in range(capacity, weight[i] - 1, -1):
        dp[w] = max(dp[w], value[i] + dp[w - weight[i]])

print("Maximum Medical Value:", dp[capacity])