__author__ = 'student'
a=[1,7,5,6,4,9,8,2,1,6]
for i in range(0,len(a)-1,1):
    if a.count(a[i])==1:
        print(a[i])