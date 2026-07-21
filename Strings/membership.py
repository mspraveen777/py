# text = "Praveen"
# print("P" in text )
# print("z" in text)
# print("z" not in text)
# print("P" not in text)
# print("vee" in text)

# in text = Programming count the number of vowels

string = "ProgrAmming"
vowels = "aeiouAEIOU"
count = 0
for ch in string:
    if ch in vowels:
        count+=1
print(count)