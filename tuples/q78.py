"""
Write the func get_stats(nums) which takes the tuple of numbers and return the tuple containig
average,sum, minimum and maximum number.Unpack the returned tuple and print the each value
"""

def get_stats(nums):
    total = sum(nums)
    avg = total/len(nums)
    mini  = min(nums)
    maxi = max(nums)
    return total,avg,mini,maxi
nums = 10,20,30,40,100
a,b,c,d = get_stats(nums)

print(f"total = {a}")
print(f"average = {b}")
print(f"min number = {c}")
print(f"max number = {d}")