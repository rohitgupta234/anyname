# Question 17: Sum of the squares of even numbers and the sum of the cubes of odd numbers in the list.
l=list(map(int,input().split()))
print(l)
a=0
b=0
for i in l:
    if i%2==0:
        a+=i**2
    else:
        b+=i**3
print(a)
print