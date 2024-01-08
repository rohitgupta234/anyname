l1=[1,2,3,4,5]
l2=[2,3,4,7,8,9]
i=[]
for j in l1:
    if j in l2 and j not in i:
        i.append(j)
print(i)