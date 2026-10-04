n = int(input("Enter number of locations: "))

cost = []

print("Enter travel cost matrix:")
for i in range(n):
    cost.append(list(map(int, input().split())))

best_cost = float('inf')
best_path = []

def solve(path, visited, total):
    global best_cost, best_path

    if len(path) == n:
        total += cost[path[-1]][path[0]]

        if total < best_cost:
            best_cost = total
            best_path = path[:]
        return

    if total >= best_cost:
        return

    for i in range(n):
        if i not in visited:
            solve(path + [i], visited | {i},
                  total + cost[path[-1]][i])

solve([0], {0}, 0)

print("\nBest Delivery Route:")
for i in best_path:
    print(i + 1, end=" -> ")
print(best_path[0] + 1)

print("Minimum Travel Cost:", best_cost)