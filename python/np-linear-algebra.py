import numpy as np
m=raw_input()
m=int(m)
arr1=[]
for i in xrange(m):
	arr1.append(map(float,raw_input().split()))
arr1=np.array(arr1)
print np.linalg.det(arr1)