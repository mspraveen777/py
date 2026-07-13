# Three methods
#POP
student = {
    "name": "Praveen",
    "gender": "Male",
    "city": "Bengaluru"
}

student.pop("name")
print(student)

##clear
#It clears entire dictionaires

# student.clear()
# print(student)

# #del
# #It deletes the variable student
del student["city"]
print(student)

# del student
# print(student) #Here student itself is deleted so  we cant perform it