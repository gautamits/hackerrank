import numpy as np
m,n=raw_input().split()
m=int(m)
n=int(n)
arr1=[]
arr2=[]
for i in xrange(m):
	arr1.append(map(int,raw_input().split()))
for i in xrange(m):
	arr2.append(map(int,raw_input().split()))
arr1=np.array(arr1)
arr2=np.array(arr2)

print arr1+arr2
print arr1-arr2
print arr1*arr2
print arr1/arr2
print arr1%arr2
print arr1**arr2
