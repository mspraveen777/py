"""
Q60. Given two lists, merge them into a single new list without modifying the originals.
"""
# 1 method
def merge_list(lst1,lst2):
    new_lst = []
    for num in lst1:
        new_lst.append(num)
    for num in lst2:
        new_lst.append(num)
    return new_lst
lst1 = [10,20,30,40,50]
lst2 = [60,70,80,90,100]
ans = merge_list(lst1, lst2)
print(ans)

# 2nd method     
def merge_two_list(lst1,lst2):
    return lst1+lst2
num1 = [10,20]
num2 = [30,40,50]
print(merge_two_list(num1,num2))
