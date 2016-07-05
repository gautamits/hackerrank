from itertools import permutations
a,b=raw_input().split()
a="".join(sorted(a))
for i in list(permutations(a,int(b))):
	print "".join(i)