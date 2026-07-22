"""
Q107. Reverse Word Order

Take a sentence as input. Reverse the order of words (not the characters in
each word). Example: "Python is fun" -> "fun is Python".
"""

def reverse_order(sentence:str):
    sentence = sentence.split()
    sentence = sentence[::-1]
    return " ".join(sentence)
   
        

sentence = "I am Praveen a Python coder"
print(reverse_order(sentence))