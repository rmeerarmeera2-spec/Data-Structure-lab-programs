patients = []

n = int(input("Enter number of patients: "))

for i in range(n):
    name = input("Enter patient name: ")
    patients.append(name)

print("Patient Queue:", patients)

print("Attending:", patients.pop(0))

print("Remaining Patients:", patients)