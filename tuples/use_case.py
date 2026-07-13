# from a list return min and max
def minmax(lst):
    mini = min(lst)
    maxi = max(lst)
    return mini,maxi         #we can return two values using tuples

ans1,ans2 = minmax([1,2,3,4,5])
print(f" The Maixmum is {ans2} and Minimum is {ans1}")
