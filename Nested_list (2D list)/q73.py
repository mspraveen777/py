"""
Q73. Given a 4x4 matrix, print only the border elements and replace the
inner elements with an asterisk (*).
"""

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

r = len(matrix)
c = len(matrix[0])
for i in range(0,r):
    for j in range(0,c):
        if i == 0 or j == 0 or i == r-1 or j == c-1:
            print(matrix[i][j],end=" ")
        else:
            print("*",end=" ") 
    print()