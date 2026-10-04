def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left = [x for x in data[1:] if x[1] <= pivot[1]]
    right = [x for x in data[1:] if x[1] > pivot[1]]

    return quick_sort(left) + [pivot] + quick_sort(right)


ambulances = []

n = int(input("Enter number of ambulances: "))

for i in range(n):
    name = input("Enter ambulance name: ")
    priority = int(input("Enter emergency priority (1-5): "))
    ambulances.append([name, priority])

ambulances = quick_sort(ambulances)

print("\nAmbulance Dispatch Order:")
for a in ambulances:
    print(a[0], "- Priority:", a[1])