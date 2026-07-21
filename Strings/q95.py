"""
Read a sentence from user.Count the number of vowels present in it, using for loop
"""

def no_of_vowels(sentence):
    count = 0
    for ch in sentence:
        if ch in "aeiouAEIOU":
            count+=1
    return count
ans = no_of_vowels("I am Praveen M Sunagar")
print(ans)