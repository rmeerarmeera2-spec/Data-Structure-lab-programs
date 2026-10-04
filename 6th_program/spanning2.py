graph = [
    [0, 4, 3, 0, 0],
    [4, 0, 2, 5, 0],
    [3, 2, 0, 3, 6],
    [0, 5, 3, 0, 7],
    [0, 0, 6, 7, 0]
]

n = len(graph)
visited = [False] * n
visited[0] = True
cost = 0

for _ in range(n - 1):
    minimum = 999
    x = y = 0

    for i in range(n):
        if visited[i]:
            for j in range(n):
                if not visited[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x, y = i, j

    print("Building", x, "-- Building", y, "Cost:", minimum)
    cost += minimum
    visited[y] = True

print("Minimum Cable Cost:", cost)