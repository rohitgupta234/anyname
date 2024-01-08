l=list(map(int, input().split()))
print(l)
min=l[0]
for i in l:
    if min>i:
        min=i
print(min)