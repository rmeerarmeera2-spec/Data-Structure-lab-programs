n = int(input("Enter number of courses: "))

course = []
print("Enter course name, credits and benefit:")

for i in range(n):
    name = input("Course name: ")
    credit = int(input("Credits: "))
    benefit = int(input("Benefit: "))
    course.append([name, credit, benefit])

limit = int(input("Enter maximum credits: "))

best_benefit = 0
best_courses = []

def branch_bound(index, credits, benefit, selected):
    global best_benefit, best_courses

    if credits > limit:
        return

    if benefit > best_benefit:
        best_benefit = benefit
        best_courses = selected[:]

    if index == n:
        return

    # Select current course
    branch_bound(
        index + 1,
        credits + course[index][1],
        benefit + course[index][2],
        selected + [course[index][0]]
    )

    # Skip current course
    branch_bound(
        index + 1,
        credits,
        benefit,
        selected
    )

branch_bound(0, 0, 0, [])

print("\nSelected Courses:")

for name in best_courses:
    print("-", name)

print("Maximum Benefit:", best_benefit)