def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left = [x for x in data[1:] if x[1] <= pivot[1]]
    right = [x for x in data[1:] if x[1] > pivot[1]]

    return quick_sort(left) + [pivot] + quick_sort(right)


crops = []

n = int(input("Enter number of crops: "))

for i in range(n):
    name = input("Enter crop name: ")
    price = int(input("Enter price per kg: "))
    crops.append([name, price])

crops = quick_sort(crops)

print("\nAgriculture Market Price:")
for c in crops:
    print(c[0], "- Rs.", c[1])