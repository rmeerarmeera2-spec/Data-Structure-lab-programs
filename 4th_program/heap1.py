heap = []

def insert(x):
    heap.append(x)
    i = len(heap) - 1

    while i > 0:
        parent = (i - 1) // 2

        if heap[parent] <= heap[i]:
            break

        heap[parent], heap[i] = heap[i], heap[parent]
        i = parent


def delete():
    if not heap:
        print("Heap is Empty")
        return

    print("Deleted:", heap[0])

    heap[0] = heap[-1]
    heap.pop()

    i = 0

    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        small = i

        if left < len(heap) and heap[left] < heap[small]:
            small = left

        if right < len(heap) and heap[right] < heap[small]:
            small = right

        if small == i:
            break

        heap[i], heap[small] = heap[small], heap[i]
        i = small


n = int(input("Enter number of elements: "))

for i in range(n):
    x = int(input("Enter element: "))
    insert(x)

print("Heap after insertion:", heap)

delete()

print("Heap after deletion:", heap)