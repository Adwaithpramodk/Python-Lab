print("--- Student Grade Manager ---")

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    grade = float(input("Enter Mark: "))
    students[name] = grade


total = sum(students.values())
avg = total / len(students)

topper = max(students, key=students.get)

print("--- Results ---")
print("Average Grade:", round(avg, 2))
print("Topper:", topper, "-", students[topper])