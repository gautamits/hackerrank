from itertools import combinations
a,b=raw_input().split()
a="".join(sorted(a))
for j in xrange(1,int(b)+1):
	for i in list(combinations(a,j)):
		print "".join(i)