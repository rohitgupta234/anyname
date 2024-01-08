# creating list using input
n=int(input("enter the value of n=> "))
list=[]
for i in range(n):
    items=int(input("enter the value of items {i+1}:"))
    list.append(items)
print(list)
