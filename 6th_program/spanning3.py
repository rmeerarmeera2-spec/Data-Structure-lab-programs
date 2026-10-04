graph = [
    [0, 7, 3, 0],
    [7, 0, 2, 5],
    [3, 2, 0, 4],
    [0, 5, 4, 0]
]

visited = [True, False, False, False]
cost = 0

for _ in range(3):
    minimum = 999

    for i in range(4):
        if visited[i]:
            for j in range(4):
                if not visited[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x, y = i, j

    print("Area", x, "-- Area", y, "Cost:", minimum)
    cost += minimum
    visited[y] = True

print("Minimum Pipeline Cost:", cost)