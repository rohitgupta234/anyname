l1=[1,2,3,4,5]
l2=[2,3,4,5]
u=[]
for i in l1+l2:
    if i not in u :
        u.append(i)
print(u)