n = int(input("Enter number of scenes: "))

cost = []

print("Enter scene transition cost matrix:")
for i in range(n):
    cost.append(list(map(int, input().split())))

best_cost = float('inf')
best_order = []

def solve(order, used, total):
    global best_cost, best_order

    if len(order) == n:
        if total < best_cost:
            best_cost = total
            best_order = order[:]
        return

    if total >= best_cost:
        return

    last = order[-1]

    for i in range(n):
        if i not in used:
            solve(
                order + [i],
                used | {i},
                total + cost[last][i]
            )

solve([0], {0}, 0)

print("\nBest Scene Order:")
for scene in best_order:
    print("Scene", scene + 1, end=" -> ")

print("\nMinimum Production Cost:", best_cost)