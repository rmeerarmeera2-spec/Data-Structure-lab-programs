graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    graph[i] = []

e = int(input("Enter number of edges: "))

for i in range(e):
    a = int(input("Enter first vertex: "))
    b = int(input("Enter second vertex: "))

    graph[a].append(b)
    graph[b].append(a)

print("\nGraph:")
for v in graph:
    print(v, ":", graph[v])


# BFS
def bfs(start):
    visited = []
    queue = [start]

    while queue:
        v = queue.pop(0)

        if v not in visited:
            visited.append(v)
            queue.extend(graph[v])

    print("BFS:", visited)


# DFS
def dfs(v, visited):
    visited.append(v)
    for x in graph[v]:
        if x not in visited:
            dfs(x, visited)


start = int(input("\nEnter starting vertex: "))

bfs(start)

visited = []
dfs(start, visited)
print("DFS:", visited)