l=list(map(int,input().split()))
print(l)
r=[]
for i in range(len(l)-1,-1,-1):
    r.append(l[i])
print(r)