# using for loop
text = "Programming"
n = len(text)
# count = 0
# for i in range(0,n):
#     if text[i]=="m"or text[i]=="M":
#         count +=1
# print(count)
     

# for char in text:
#     print(char)
ch = 0
while ch <= n-1:
    print(text[ch],end=" ")
    ch+=1
print()
for ind,ch in enumerate(text):
    print(f"Index = {ind} and Char = {ch}")
