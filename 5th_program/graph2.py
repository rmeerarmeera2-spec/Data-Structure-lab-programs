graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B"],
    "E": ["C"]
}

def bfs(start):
    visited = []
    queue = [start]

    while queue:
        x = queue.pop(0)
        if x not in visited:
            visited.append(x)
            queue += graph[x]

    return visited

print("Friends Network:", bfs("A"))