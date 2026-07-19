"""
Create the nested dictinary containg details for 4 students, where each student entry
includes their name, age and city. Write a loop to print the full details of each student
in clear and readable format.
"""

students = {
    101: {"name": "Pravin", "age": 23, "city": "Bengaluru"},
    102: {"name": "Rahul", "age": 22, "city": "Pune"},
    103: {"name": "Suraj", "age": 21, "city": "Delhi"},
    104: {"name": "Basu", "age": 25, "city": "Mumbai"},
}
for roll_no,details in students.items():
    print(f"Roll no: {roll_no} and Details: {details}")