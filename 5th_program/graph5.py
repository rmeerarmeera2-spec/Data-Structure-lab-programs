graph = {
    "Home": ["Profile", "Settings"],
    "Profile": ["Photos"],
    "Settings": ["Help"],
    "Photos": [],
    "Help": []
}

start = input("Enter starting screen: ")

visited = []

def dfs(node):
    visited.append(node)

    for screen in graph[node]:
        if screen not in visited:
            dfs(screen)

dfs(start)

print("Screen Navigation:", visited)