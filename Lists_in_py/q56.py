"""
Given two lists of the same length, write Python code using a loop to create
a new list where each element is the sum of the corresponding elements from
both original lists.
"""



# num = []
# n = len(lst1)
# for i in range(0,n):
#     total = lst1[i]+lst2[i]
#     num.append(total)
# print(num)
    

def average(lst1,lst2):
    num = []
    n = len(lst1)
    for i in range(0,n):
        total = lst1[i] + lst2[i]
        num.append(total)
    return num
lst1 = [10,20,30,40,50]
lst2 = [60,70,80,90,100]
ans =average(lst1,lst2)
print(ans)