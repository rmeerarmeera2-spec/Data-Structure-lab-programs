graph = {
    "Level1": ["Level2", "Level3"],
    "Level2": ["Level4"],
    "Level3": ["Level5"],
    "Level4": [],
    "Level5": []
}

start = input("Enter starting level: ")

visited = []

def dfs(node):
    visited.append(node)

    for next_node in graph[node]:
        if next_node not in visited:
            dfs(next_node)

dfs(start)

print("Game Path:", visited)