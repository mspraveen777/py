"""
Using a dictionary comphernsion , create a new dictionary where keys and numbers from 1 to 10
(inclusive), values are cube of each number.
"""

cubes = {i:i**3 for i in range(1, 11)}
print(cubes)