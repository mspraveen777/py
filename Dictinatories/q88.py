"""
Q88. Student Marks Analysis

Design a dictionary where each key is a student's name and the corresponding
value is a list of their marks in 3 different subjects. Calculate and print
the total marks and average marks for each student.
"""

students = {
    "Praveen": [98, 78, 89],
    "Akash": [89, 95, 99],
    "Suraj": [95, 62, 48],
    "Harish": [88, 78, 65],
}
for name,marks in students.items():
    total = sum(marks)
    avg = total/len(students)
    print(f"{name} scored Total Marks: {total} and Average marks: {avg}")