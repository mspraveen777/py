"""
Q58. Find the largest and smallest number in a list without using built-in functions
like max() or min().
"""

lst = [-1111.111,10,56,89,45,2,365,456,999.9999]
def largest_smallest(lst):
    largest = float("-inf")
    smallest = float("+inf")
    for num in lst:
        if num > largest:
                largest = num

        
    for num in lst:
        if num < smallest:
                smallest = num
    return f"largest = {largest} and smallest = {smallest}"
a = largest_smallest(lst)
print(a)