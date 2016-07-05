import numpy as np
m=raw_input()
m=int(m)
arr1=[]
arr2=[]
for i in xrange(m):
	arr1.append(map(int,raw_input().split()))
for i in xrange(m):
	arr2.append(map(int,raw_input().split()))
arr1=np.array(arr1)
arr2=np.array(arr2)
print arr1
print arr2
print np.matrix(arr1)*np.matrix(arr2)