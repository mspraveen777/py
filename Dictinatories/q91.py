"""
Given an existing dictionary of subjects and their respective marks, use dicitionary
comprehension to generate new dictionary that only the subjects the students scored 40
or more(i.e. passed).

"""

marks = {
    "science": 90,
    "math": 39,
    "hindi": 35,
    "english": 78,
    "social": 85,
}

passed = {subject:mark for subject,mark in marks.items() if mark >=40}
print(passed)
