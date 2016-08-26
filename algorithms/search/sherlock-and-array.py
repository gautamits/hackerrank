t=int(raw_input())
for _ in xrange(t):
	raw_input()
	arr=map(int,raw_input().split())
	s=sum(arr)
	t=0
	for i in xrange(len(arr)):
		if t==s-arr[i]-t:
			print 'YES'
			break
		elif i+1==len(arr):
			print "NO"
			break
		else:
			t=t+arr[i]
