"""
Q59. Reverse a list without using the .reverse() method or list slicing ([::-1]).
"""

lst = [10,20,55,6,77,98,9]
def revrese_no(lst):
    n = len(lst)
    new_lst = []
    for i in range(n-1,-1,-1):
        new_lst.append(lst[i])
    return new_lst
a = revrese_no(lst)
print(a)

