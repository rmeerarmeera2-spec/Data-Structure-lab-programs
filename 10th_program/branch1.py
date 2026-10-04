import heapq

n = int(input("Enter number of employees/tasks: "))

cost = []

print("Enter cost matrix:")
for i in range(n):
    row = list(map(int, input(f"Employee {i + 1}: ").split()))
    cost.append(row)

pq = []
heapq.heappush(pq, (0, 0, [], set()))

best_cost = float('inf')
best_assignment = []

while pq:
    current_cost, employee, assignment, used = heapq.heappop(pq)

    if current_cost >= best_cost:
        continue

    if employee == n:
        best_cost = current_cost
        best_assignment = assignment
        continue

    for task in range(n):
        if task not in used:
            new_cost = current_cost + cost[employee][task]

            if new_cost < best_cost:
                new_assignment = assignment + [task]
                new_used = used | {task}

                heapq.heappush(
                    pq,
                    (new_cost, employee + 1, new_assignment, new_used)
                )

print("\nOptimal Job Allocation:")
for i in range(n):
    print("Employee", i + 1, "-> Task", best_assignment[i] + 1)

print("Minimum Total Cost:", best_cost)