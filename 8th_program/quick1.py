def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    left = [x for x in data[1:] if x[2] <= pivot[2]]
    right = [x for x in data[1:] if x[2] > pivot[2]]

    return quick_sort(left) + [pivot] + quick_sort(right)


bookings = []

n = int(input("Enter number of bookings: "))

for i in range(n):
    print("\nBooking", i + 1)

    name = input("Enter customer name: ")
    movie = input("Enter movie name: ")
    price = int(input("Enter ticket price: "))

    bookings.append([name, movie, price])

sorted_bookings = quick_sort(bookings)

print("\n--- Sorted Movie Ticket Bookings ---")

for b in sorted_bookings:
    print("Name:", b[0], "| Movie:", b[1], "| Price:", b[2])