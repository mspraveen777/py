# Set operators
# Union (| or .union())
a = {10, 20, 30}
b = {20, 30, 40, 50}
# print(a | b)
print(a.union(b))

# intersection ( & or .intersection())
a = {10, 20, 30, 40}
b = {20, 30, 40, 50}
# print(a & b)
print(a.intersection(b))

# real world example
math_Students = {"Pravin", "Suraj", "Rahul", "Mahesh", "siddu"}
science_Students = {"Mahesh", "Raju", "Pravin", "akash", "Ravi", "Suraj"}
#print the students those studies both maths and science
print(math_Students & science_Students)