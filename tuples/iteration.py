my_tuples = ("Pravin",162,18.20,"Raju")
# for i in range(0,4):           # method 1
#     print(my_tuples[i],end=" ")

# for ele in my_tuples:              # method 2
#     print(ele,end=" ")
for index,value in enumerate(my_tuples):
    print(f"Index = {index} and value = {value}")