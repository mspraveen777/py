"""
Q62. Separate a list of integers into two distinct lists: one containing all the
even numbers and the other containing all the odd numbers.
"""


def is_even_odd(lst):
    even = []
    odd = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return f"even list = {even}\nodd list = {odd}"
lst = [10,22,31,85,68,94,21,325,48,47,77]
ans = is_even_odd(lst)
print(ans)