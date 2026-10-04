import heapq

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    heapq.heappush(students, (-marks, name))

print("\nStudent Ranking:")

while students:
    marks, name = heapq.heappop(students)
    print(name, "-", -marks)