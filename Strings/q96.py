"""
Given a string input. print every alternative charcter start with very first charcter
using string slicing
"""

def alternative(str):
    return str[::2]
ans = alternative("I am Praveen Sunagar a coder")
print(ans)