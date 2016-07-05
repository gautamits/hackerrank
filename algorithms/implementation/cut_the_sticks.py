def cut(a):
	if len(a)==0:
		exit(0)
	elif len(a)==1:
		print 1
		exit(0)
	print len(a)
	s=a[0]
	a=[(i-s) for i in a]
	indexes=a.count(0)
	a=a[indexes:]
	cut(a)
t=int(raw_input())
a=raw_input().split()
a=[int(i) for i in a]
a=sorted(a)
cut(a)
