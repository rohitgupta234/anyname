l=list(map(int,input().split()))
print(l)
a=0
b=0
for i in l:
    if i%2==0:
        a+=1
    else:
        b+=1
print(a)
print(b)