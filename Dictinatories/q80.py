"""
Define dicitinory with a five subjects and their respective marks.Utilize the get()
method to accessing the subject that is not in dicitionary, ensure it will print
"Not Available" as default
"""

marks = {
    "Science": 97,
    "Maths": 89,
    "English": 88,
    "Kannada": 100,
    "Computer Science": 75,
}
s = input("enter the subject: ")
# print(marks.get("Maths"))
print(marks.get(s, "Not Available"))
