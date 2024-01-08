l=list(map(int,input().split()))
print(l)
a=0
b=0
for i in l:
    if i%2==0:
        a+=i
    else:
        b+=i
print(a)
print(b)