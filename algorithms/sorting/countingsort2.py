n=raw_input()
arr=raw_input().split()
arr=[int(i) for i in arr]
a=[0]*100
for i in arr:
	a[i]=a[i]+1
for i in xrange(len(a)):
	r=a[i]
	j=0
	while j < r:
		print i,
		j+=1