l=list(map(int,input().split()))
print(l)

p=True
for i in range(len(l)//2):
    if l[i]!=l[-i-1]:
        p=False
        break
if p:
    print("palindrone")
else:
    print("not palindrone")