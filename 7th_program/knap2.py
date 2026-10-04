items = ["Laptop", "Camera", "Shoes", "Book"]
weight = [3, 2, 2, 1]
value = [60, 50, 30, 20]

capacity = int(input("Enter bag capacity: "))

dp = [0] * (capacity + 1)

for i in range(4):
    for w in range(capacity, weight[i] - 1, -1):
        dp[w] = max(dp[w], value[i] + dp[w - weight[i]])

print("Maximum Travel Value:", dp[capacity])