"""
Take a name as a input from user. Print its first charcter ,last charcter 
and total length of the name.
"""
# name = str(input("Enter the name: "))
# print(f"first char:  {name[0]}")
# print(f"last char:  {name[-1]}")
# print(f" length: {len(name)}")

def print_details(name):
    first = name[0]
    last = name[-1]
    n = len(name)
    print(f" First= {first} last= {last} and length= {n}")
print_details("Praveen")