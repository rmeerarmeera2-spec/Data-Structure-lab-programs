n = int(input("Enter number of vertices: "))

graph = []

print("Enter the weighted graph:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

visited = [False] * n
visited[0] = True

edges = 0
cost = 0

print("\nMinimum Spanning Tree:")

while edges < n - 1:
    minimum = 999
    x = 0
    y = 0

    for i in range(n):
        if visited[i]:
            for j in range(n):
                if not visited[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(x, "--", y, "=", minimum)

    cost += minimum
    visited[y] = True
    edges += 1

print("Minimum Cost:", cost)