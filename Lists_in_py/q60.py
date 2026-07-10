"""
Q60. Given two lists, merge them into a single new list without modifying the originals.
"""

def merge_list(lst1,lst2):
    new_lst = lst1.copy()
    n = len(lst2)
    for i in range(0,n):
        new_lst.append(lst2[i])
    return new_lst
lst1 = [10,20,30,40,50]
lst2 = [60,70,80,90,100]
ans = merge_list(lst1, lst2)
print(ans)
        

