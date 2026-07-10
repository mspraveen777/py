"""
Q65. Write a Python script that iterates through a list of integers and replaces every
negative number found in the list with the value 0.
"""


def replace_negative(lst):
    n = len(lst)
    for i in range(0,n):
        if lst[i] < 0:
            lst[i] = 0
    return lst


lst = [10,-2,-20,-43,56,-7,-89]
ans = replace_negative(lst)
print(ans)