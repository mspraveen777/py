#sort vs sorted

lst = [2,3,4,3,5,3,7,8,89,75.45,97,44,4]

print(lst)
# new_lst = sorted(lst)  # it is new list 
# print(new_lst)

lst.sort()
print(lst)  # it is in list sorting

lst.sort(reverse=True)
print(lst)  # it is in list sorting
