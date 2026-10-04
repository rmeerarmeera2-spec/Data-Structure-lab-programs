def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left = [x for x in data[1:] if x[1] <= pivot[1]]
    right = [x for x in data[1:] if x[1] > pivot[1]]

    return quick_sort(left) + [pivot] + quick_sort(right)


products = []

n = int(input("Enter number of products: "))

for i in range(n):
    name = input("Enter product name: ")
    price = int(input("Enter product price: "))
    products.append([name, price])

products = quick_sort(products)

print("\nProducts Sorted by Price:")
for p in products:
    print(p)