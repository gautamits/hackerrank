from itertools import combinations_with_replacement
a,b=raw_input().split()
a="".join(sorted(a))
for i in list(combinations_with_replacement(a,int(b))):
	print "".join(i)