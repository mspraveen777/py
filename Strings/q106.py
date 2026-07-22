"""
Q106. Word Lengths (Homework)

Take a sentence as input. Print each word's length next to it.
Example: Python (6) is (2) great (5).
"""

sentence = "Praveen is learning Python programming every single day"

def words_length(sentence):
    sentence = sentence.split()
    for word in sentence:
        print(f"{word} ({len(word)}) ",end=" " )
words_length(sentence)