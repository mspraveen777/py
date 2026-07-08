age  = 23
def func():
    global age  ## using this keyword we can change the
                ## value of global variable.
    age = 30
    print(age)
func()
print(age)
