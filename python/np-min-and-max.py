import numpy as np
m,n=raw_input().split()
m=int(m)
n=int(n)
arr=[]
for i in xrange(m):
	arr.append(map(int,raw_input().split()))
print np.max(np.min(np.array(arr),axis=1))