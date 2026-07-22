"""
Q105. Palindrome Check

Write a function is_palindrome(text) that returns True if the given string is
a palindrome (ignoring case and spaces).
"""

def is_palindrome(text):
    text = text.lower().replace(" ","")
    if text == text[::-1]:
        return True
    return False
text = "raCecar"
print(is_palindrome(text))   