"""
Write a program that takes a list of numbers and, using a loop, determines
whether it is sorted in ascending order. Print True if it is sorted,
and False otherwise.
"""

def is_sorted(lst):
    n = len(lst)
    for i in range(0,n-1):
        if lst[i] > lst[i + 1]:
            return False
    return True
lst = [10,20,30,50,40]
print(is_sorted(lst))