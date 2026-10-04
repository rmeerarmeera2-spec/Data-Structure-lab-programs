import heapq

patients = []

n = int(input("Enter number of patients: "))

for i in range(n):
    name = input("Enter patient name: ")
    priority = int(input("Enter priority (1=Emergency): "))
    heapq.heappush(patients, (priority, name))

print("\nTreatment Order:")

while patients:
    priority, name = heapq.heappop(patients)
    print(name, "- Priority:", priority)