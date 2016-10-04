__author__ = 'student'
a=[2,7,5,6,4]
for i in range(1,len(a),2):
    a[i-1],a[i]=a[i],a[i-1]
print(a)
