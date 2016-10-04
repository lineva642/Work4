__author__ = 'student'
a=[1,2,3,4,5]
b=a[len(a)//2+1:len(a)]
m=b[::-1]
for i in range(len(a)//2):
    a.insert(1+2*i,m[i])
print(a[0:len(a)-len(m)])