# for checking

text = "Praveen Sunagar"

# print(text.isalpha())
# print(text.isdigit())
# print(text.isalnum())
# print(text.isspace())
# print(text.startswith("P"))
print(text.endswith("gar"))


#example

age = input("Enter the age: ")
if age.isdigit():
    if int(age) >= 18:
        print("You can vote")
    else:
        print("You cannot vote")
else:
    print("Plz enter proper age")