n = int(input("Enter number of items: "))

weight = []
profit = []

for i in range(n):
    w = int(input("Enter weight: "))
    p = int(input("Enter profit: "))
    weight.append(w)
    profit.append(p)

capacity = int(input("Enter bag capacity: "))

dp = [0] * (capacity + 1)

for i in range(n):
    for w in range(capacity, weight[i] - 1, -1):
        dp[w] = max(dp[w], profit[i] + dp[w - weight[i]])

print("Maximum Profit:", dp[capacity])