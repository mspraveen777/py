#  strings are immutable

name = "Praveen"
print(name , id(name))

# name[0]= "a"  # string cannot support this

name = "Pravin"
print(name, id(name)) # here string is overrided  not updated, thier id are different