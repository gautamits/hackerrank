for _ in xrange(int(raw_input())):
	n=int(raw_input())
	arr=map(int,raw_input().split())
	a=arr[0]
	for i in xrange(1,n):
		a=a|arr[i]
	print a*2**(n-1)