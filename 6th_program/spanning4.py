graph = [
    [0, 4, 3, 0, 0],
    [4, 0, 5, 2, 0],
    [3, 5, 0, 6, 4],
    [0, 2, 6, 0, 7],
    [0, 0, 4, 7, 0]
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

    print("Street", x, "-- Street", y, "Cost:", minimum)
    cost += minimum
    visited[y] = True

print("Minimum Wiring Cost:", cost)