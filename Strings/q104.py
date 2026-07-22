"""
Q104. Unique Words Count

Take a paragraph as input. Print the count of unique words in it
(case insensitive).
"""

def unique_words(paragraph):
    count = 0
    unique = ""
    paragraph = paragraph.split()
    print(len(sorted(set(paragraph))))
    
paragraph = "Praveen is coder and he is developer and he is programmer "
unique_words(paragraph)