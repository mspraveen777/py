"""
Q72. Given a 3x3 matrix, print only the anti-diagonal (top-right to bottom-left)
elements and replace everything else with an asterisk (*).

1  2 3
4  5 6
7  8 9

Expected Output:
*  * 3
*  5 *
7  * *
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

rows = len(matrix)
col = len(matrix[0])
for i in range(0, rows):
    for j in range(0, col):
        if i + j == col - 1:  # it is equal to 2 for 4x4 matrix it should 3 so row -1
            # or col - 1
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")
    print()
