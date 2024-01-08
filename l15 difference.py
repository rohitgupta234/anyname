# Question 14: Find the Difference (Uncommon elements) between Two Lists
l1=[1,2,3,4,5,6]
l2=[3,4,5,6,7,8]
d=[i for i in l1+l2 if i not in l1 or i not in l2]
print(d)