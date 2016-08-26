n=int(raw_input())
a=[0]*100
for i in xrange(n):
	i,j=raw_input().split()
	i=int(i)
	a[i]=a[i]+1
for i in xrange(1,100):
	a[i]=a[i-1]+a[i]
print " ".join(map(str,a))