n = int(input("Enter number of videos: "))

weight = []
value = []

for i in range(n):
    weight.append(int(input("Enter video size: ")))
    value.append(int(input("Enter video priority: ")))

capacity = int(input("Enter storage capacity: "))

dp = [0] * (capacity + 1)

for i in range(n):
    for w in range(capacity, weight[i] - 1, -1):
        dp[w] = max(dp[w], value[i] + dp[w - weight[i]])

print("Maximum Video Priority:", dp[capacity])