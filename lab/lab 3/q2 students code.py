# Create a dictionary of students with their grades
students = {
    "Monik": "A",
    "Tony": "B",
    "Charlie": "A",
    "Steve": "C",
    "Paper": "B"
}

# 1. Display all students with their grades
print("Students and their grades:")
for student, grade in students.items():
    print(student, grade)

# 2. Add a new student with their grade
students["Thor"] = "A"
print("\nAdded a new student:")
print(students)

# 3. Update the grade of an existing student
students.update({"Paper": "A"})
print("\nUpdated Paper's grade:")
print(students)

# 4. Remove a student
students.pop("Charlie")
print("\nRemoved Bob from the list:")
print(students)

# 5. Display all students again after updates
print("\nUpdated list of students and their grades:")
for student, grade in students.items():
    print(student, grade)
