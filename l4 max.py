l=list(map(int, input().split()))
print(l)
max=l[0]
for i in l:
    if max<i:
        max=i
print(max)