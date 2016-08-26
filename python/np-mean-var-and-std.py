import numpy as np
m,n=raw_input().split()
m=int(m)
n=int(n)
arr=[]
for i in xrange(m):
	arr.append(map(int,raw_input().split()))
print np.mean(np.array(arr),axis=1)
print np.var(np.array(arr),axis=0)
print np.std(np.array(arr))