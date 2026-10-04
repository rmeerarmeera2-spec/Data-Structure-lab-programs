queue = []
print("QUEUE")
queue.append(10)
queue.append(20)
queue.append(30)
print("After Insertion:", queue)
print("Deleted:", queue.pop(0))
print("After Deletion:", queue)
cqueue = [10, 20, 30]
print("\nCIRCULAR QUEUE")
print("Before Deletion:", cqueue)
cqueue.pop(0)
cqueue.append(40)
print("After Insertion and Deletion:", cqueue)