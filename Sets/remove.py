# removing elements in sets

# remove
fruits = {"apple", "kiwi", "mangao", "orange", "litchi"}
fruits.remove("apple")
print(fruits)

# discard
fruits.discard(
    "litchi"
)  # if the elements exist it will remove else it will not give error
print(fruits)

# pop
fruits.pop()
print(fruits)

fruits.clear()
print(fruits)
