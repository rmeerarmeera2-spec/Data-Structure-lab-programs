import heapq

cabs = []

n = int(input("Enter number of cabs: "))

for i in range(n):
    name = input("Enter driver name: ")
    distance = int(input("Enter distance from customer: "))
    heapq.heappush(cabs, (distance, name))

print("\nNearest Cab:")

distance, name = heapq.heappop(cabs)
print(name, "is", distance, "km away")