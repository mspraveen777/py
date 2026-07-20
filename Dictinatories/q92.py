"""
You have two separate list; one containing subject names and another containing corresponding marks.
Create a dictionary into list  using a dict comprehension, mapping  each to its marks.
"""
subjects = ["science","math","english","kannada","hindi"]
marks = [99,89,78,100,65]


dict = {subjects:marks for subjects,marks in zip(subjects,marks)}
# dict = dict(zip(subjects,marks))
print(dict)