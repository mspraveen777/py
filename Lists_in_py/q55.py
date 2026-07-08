"""
Given a list of numbers, use a loop to calculate and print their average.
You can use len() to get the count of elements, but avoid using
sum() for the total.
"""

def average(nums):
    n  = len(nums)
    total = 0
    for num in nums:
        total += num
    average = total/n
    return average
nums = [10,20,30,40,50]
ans = average(nums)
print(f"average is {ans:.2f}")

