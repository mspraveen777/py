my_tuple = (1, 2, 3, 4)
print(my_tuple)

my_tuple = 1, 2, 3, 4  # here also it will store as tuple
print(my_tuple)

a = 1  # but when it comes to 1 element it will store as value assigning as int
print(a)

a = (1,)  # to make it tuple add one ,(comma) to it
print(a)
print(type(a))

a ,b,c = (1,2,"Pravin")   # Here tuples are unpacked and stored ato individual variable as int
print(a,)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))