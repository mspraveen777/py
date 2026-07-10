"""
Q63. Create a list containing the squares of numbers from
1 to 10 (i.e., [1, 4, 9, ..., 100]).
"""

def squares():
    squares = []
    for i in range(1,11):
        squares.append(i**2)
    return squares

print(squares())