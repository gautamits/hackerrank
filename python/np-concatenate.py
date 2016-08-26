import numpy as np
m,n,p=raw_input().split()
m=int(m)
n=int(n)
p=int(p)
arr1=[]
arr2=[]
for i in xrange(m):
	arr1.append(map(int,raw_input().split()))
for i in xrange(n):
	arr2.append(map(int,raw_input().split()))
print np.concatenate((np.array(arr1),np.array(arr2)),axis=0)