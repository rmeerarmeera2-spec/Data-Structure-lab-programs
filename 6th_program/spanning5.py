graph = [
    [0, 8, 5, 0, 0],
    [8, 0, 3, 6, 0],
    [5, 3, 0, 4, 7],
    [0, 6, 4, 0, 2],
    [0, 0, 7, 2, 0]
]

visited = [True, False, False, False, False]
cost = 0

for _ in range(4):
    minimum = 999

    for i in range(5):
        if visited[i]:
            for j in range(5):
                if not visited[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x, y = i, j

    print("Station", x, "-- Station", y, "Cost:", minimum)
    cost += minimum
    visited[y] = True

print("Minimum Railway Cost:", cost)