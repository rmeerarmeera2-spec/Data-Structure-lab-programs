import heapq

packages = []

n = int(input("Enter number of packages: "))

for i in range(n):
    name = input("Enter package name: ")
    priority = int(input("Enter priority (1=Urgent): "))
    heapq.heappush(packages, (priority, name))

print("\nDelivery Order:")

while packages:
    priority, name = heapq.heappop(packages)
    print(name, "- Priority:", priority)