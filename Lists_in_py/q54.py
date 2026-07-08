# Target existenxe
my_list = [10,20,30,40,50]
target = 60

def is_exists(my_list,target):
    for num in my_list:
        if num == target:
            return f"Target {target} exist in the loop"
    return f"Target {target} not exist in the loop"

    
print(is_exists(my_list,target))

