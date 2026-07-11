# if matrix is like 4X5

matrix = [
    [1, 2, 3, 4, 5],
    [5, 6, 7, 8, 9],
    [6, 8, 3, 2, 1],
    [3, 4, 6, 8, 9],
]

# for that we make rows and columns

rows = len(matrix)
columns = len(matrix[0])
total = 0

for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=" ")  # If we want to print list elments
        total += matrix[i][j]  # If we want to print total
    print()
print(total)
