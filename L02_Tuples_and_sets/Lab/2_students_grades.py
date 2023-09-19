number_students = int(input())
students_grades = {}

for student in range(number_students):
    student_name, grade = input().split()
    grade = float(grade)
    if student_name not in students_grades:
        students_grades[student_name] = []
        students_grades[student_name].append(grade)
        continue

    students_grades[student_name].append(grade)

for student, grades in students_grades.items():
    grades_string = ' '.join(f"{grade:.2f}" for grade in grades)
    average_grade = sum(grades) / len(grades)
    print(f"{student} -> {grades_string} (avg: {average_grade:.2f})")

# Write a program that reads students' names and their grades and adds them to the student record.
# On the first line, you will receive the number of students – N.
# On the following N lines, you will be receiving a student's name and grade.
# For each student print all his/her grades and finally his/her average grade,
# formatted to the second decimal point in the format:
# "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
# The order in which we print the result does not matter.
#
# # Input:
#     7
#     Peter 5.20
#     Mark 5.50
#     Peter 3.20
#     Mark 2.50
#     Alex 2.00
#     Mark 3.46
#     Alex 3.00
# Output:
#     Mark -> 5.50 2.50 3.46 (avg: 3.82)
#     Peter -> 5.20 3.20 (avg: 4.20)
#     Alex -> 2.00 3.00 (avg: 2.50)

# Input:
#     4
#     Scott 4.50
#     Ted 3.00
#     Scott 5.00
#     Ted 3.66
# Output:
#     Ted -> 3.00 3.66 (avg: 3.33)
#     Scott -> 4.50 5.00 (avg: 4.75)
