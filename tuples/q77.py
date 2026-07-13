"""
Take 5 numbers as input from user,store them in tuple and print the tuple along with min
min and max number
"""
num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))
num3 = int(input("Enter the number 3: "))
num4 = int(input("Enter the number 4: "))
num5 = int(input("Enter the number 5: "))

my_tuple = num1,num2,num3,num4,num5
print(my_tuple)
mini = min(my_tuple)
maxi = max(my_tuple)
print(f"Minium Number is: {mini} and Maximum Number is {maxi}")
