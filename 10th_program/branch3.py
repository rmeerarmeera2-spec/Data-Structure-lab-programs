n = int(input("Enter number of network locations: "))

cost = []

print("Enter cable cost matrix:")
for i in range(n):
    cost.append(list(map(int, input().split())))

best = float('inf')
best_edges = []

def solve(visited, total, edges):
    global best, best_edges

    if len(visited) == n:
        if total < best:
            best = total
            best_edges = edges[:]
        return

    if total >= best:
        return

    current = list(visited)[-1]

    for i in range(n):
        if i not in visited and cost[current][i] != 0:
            solve(
                visited | {i},
                total + cost[current][i],
                edges + [(current, i)]
            )

solve({0}, 0, [])

print("\nMinimum Cable Connection:")
for a, b in best_edges:
    print("Location", a + 1, "-> Location", b + 1)

print("Minimum Cost:", best)