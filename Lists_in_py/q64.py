"""
Q64. Given a list of numbers (which may contain duplicates), write a Python script
that takes an integer as input from the user and removes all occurrences of that
integer from the list.
"""

# def remove_occurance(lst):
#     result = []
#     for num in lst:
#         if num not in result:
#             result.append(num)
#     n = int(input("Enter the number: "))
#     if n in result:
#         result.remove(n)
#     return result
# lst = [10,20,30,20,10,40,10,50]
# ans = remove_occurance(lst)
# print(ans)

def remove_occurance(lst,target):
    while target in lst:
        lst.remove(target)
    return lst
lst = [10,20,30,20,10,40,10,50]
ans = remove_occurance(lst,20)
print(ans)
