items = ["Laptop", "Headphone", "Watch", "Bag"]
cost = [50, 20, 30, 15]
value = [100, 50, 70, 30]

budget = int(input("Enter budget: "))

dp = [0] * (budget + 1)

for i in range(4):
    for b in range(budget, cost[i] - 1, -1):
        dp[b] = max(dp[b], value[i] + dp[b - cost[i]])

print("Maximum Shopping Value:", dp[budget])