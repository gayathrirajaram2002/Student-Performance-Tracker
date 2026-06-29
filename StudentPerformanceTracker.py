# Initialize lists to store student names and marks
student_names = []
student_surnames = []
student_marks = []

# Loop to get input for up to 5 students
for _ in range(5):
    name = input("Enter student name: ")
    surname = input("Enter student surname: ")
    mark = int(input("Enter student mark: "))
    student_names.append(name)
    student_surnames.append(surname)
    student_marks.append(mark)

# Calculate class average
class_average = sum(student_marks) / len(student_marks)

# Find the highest and lowest marks and their corresponding student names
highest_mark = max(student_marks)
lowest_mark = min(student_marks)
highest_student_index = student_marks.index(highest_mark)
lowest_student_index = student_marks.index(lowest_mark)
highest_student = f"{student_names[highest_student_index]} {student_surnames[highest_student_index]}"
lowest_student = f"{student_names[lowest_student_index]} {student_surnames[lowest_student_index]}"

# Count number of students passed and failed
passed_count = sum(mark >= 40 for mark in student_marks)
failed_count = len(student_marks) - passed_count

# Display class statistics
print("\nClass Average:", class_average)
print("Highest Student:", highest_student, "Mark:", highest_mark)
print("Lowest Student:", lowest_student, "Mark:", lowest_mark)
print("Number Passed:", passed_count)
print("Number Failed:", failed_count)

# Display names and marks of all students
print("\nStudent Names and Marks:")
for name, surname, mark in zip(student_names, student_surnames, student_marks):
    print(f"{name} {surname}:", mark)
