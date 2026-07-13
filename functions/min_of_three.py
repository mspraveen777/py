# def min_of_three(a,b,c):
#     if a < b and a < c:
#         return a
#     elif b < c and b < a:
#         return b
#     return c
# print(f"The smallest no. is {min_of_three(30,200,1008)}")

def min_of_three(a, b,c):
    return min(a,b,c)
print(min_of_three(10,20,50))