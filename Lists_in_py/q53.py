#Find the largest element using loop dont use inbuilt func

numbers = [-1,-34,-93,-2]
maxi = float("-inf")
for number in numbers:
    if maxi < number:
        maxi = number
print(F" The largest number is {maxi}")
