def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left = [x for x in data[1:] if x[1] >= pivot[1]]
    right = [x for x in data[1:] if x[1] < pivot[1]]

    return quick_sort(left) + [pivot] + quick_sort(right)


players = []

n = int(input("Enter number of players: "))

for i in range(n):
    name = input("Enter player name: ")
    score = int(input("Enter player score: "))
    players.append([name, score])

players = quick_sort(players)

print("\nTournament Ranking:")
for i, p in enumerate(players, 1):
    print(i, p[0], "- Score:", p[1])