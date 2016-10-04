__author__ = 'student'
a=[1,7,5,6,4,9,8,2,1,6]
for i in range(0,len(a)-2,1):
    max=a[0]
    cnt=a.count(a[0])
    if cnt<a.count(a[i+1]):
        max=a[i+1]
    print(max)