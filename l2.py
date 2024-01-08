# creating a list using input without use append
n=int(input("enter the value of n=> "))
list=[0]*n
for i in range(n):
    item=input("enter the value of {i+1}:")
    list[i]=item
print(list)