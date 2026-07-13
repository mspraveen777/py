marks = {
    "science": 100,
    "maths": 98,
    102: 34,
    100: [10, 20, 30],
    #[10, 34]: 100,  #It is not possible bcz the key should be immutable
    (10, 34): 100, 
}
print(marks)
print(type(marks))
