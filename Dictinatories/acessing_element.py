students = {
    "maths": 100,
    "science": 98,
    "hindi": 95,
    1: 1990,
}
subject = "science"
# print(students["maths"])
# print(students[1])
# print(students.get("maths"))  #alternative way using get func
# print(students.get("science"))
ans = students.get(subject)
if ans is None:
    print("Subject not found")
else:
    print(ans)