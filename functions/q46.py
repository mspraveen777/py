"""
Write the func fizzbuzz(n) that takes the single number
and prints "Fizz" if it is divisible by 3 ,"Buzz" if it is 
divisble by 5,"FizzBuzz" if it is divisible by both , 
otherwise print number itself
"""
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else: 
        return n
    
res = fizzbuzz(20)
print(res)