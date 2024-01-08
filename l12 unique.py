l=[1,2,3,9,8,3,4,4,3,2,1]
u=[]
for i in l:
    if i not in u:
        u.append(i)
print(u)