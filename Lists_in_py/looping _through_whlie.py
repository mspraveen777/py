lst = [10,20,45,67,87,6,545,645,34,56,743,34,67]
n = len(lst)
# i = 0
# while i <= n-1:
#     print(lst[i], end=" ")
#     i += 1
        # print(count)

# revesing order
# i = n-1
# while i >= 0:
#     print(lst[i], end=" ")
#     i -= 1

# count of even number
i = 0
count = 0
while i <= n-1:
    if lst[i] % 2 == 0:
        count+=1
    i+=1
print(count)

