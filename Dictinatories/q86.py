"""
Create a dicitonary of 6 subjecties and their respective marks.Print the subject with the
highest marks and one with the lowest,using max() and min() functions alongside  a lambda
expression

"""

mark = {
    "science": 98,
    "math": 89,
    "english": 78,
    "hindi": 65,
    "computer science": 86,
    "kannada": 100,
}

highest = max(mark.items(),key= lambda x:x[1])
print(f" Maximunm: {highest}")

minimum = min(mark.items(), key=lambda x:x[1])
print(f"Minimun: {minimum}")