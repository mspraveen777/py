lst = [2,3,4,3,5,3,7,8,89,75.45,97,44,4]

print( 88 in lst)
print( 88 not in lst)

target = int(input("Enter the number: "))
if target in lst:
    lst.remove(target)
    print(lst)
else:
    print("Target not exist")

