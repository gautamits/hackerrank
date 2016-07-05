
from __future__ import division
n=int(raw_input())
m={}
for i in xrange(n):
	arr=raw_input().split()
	name=arr[0]
	marks=arr[1:]
	marks=[int(j) for j in marks]
	m[name]=sum(marks)/len(marks)
q=raw_input()
print('%.2' % m[q])
