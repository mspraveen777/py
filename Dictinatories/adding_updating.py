student = {
    "name": "Praveen",
    "gender": "Male",
    "city": "Bengaluru"
}
print(student,id(student))
#Update
# student["city"]= "Mysuru" 
student.update({"city":"mysore","name":"Pravin"})
print(student,id(student))
#Add
# student["Phn"]= 9740024942
student.update({"phn":"9740024942"})
print(student,id(student))


## we can update/add multiple values in update func
