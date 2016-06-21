n,o=raw_input("").split()
n=int(n)
o=int(o)
lastans=0
l=[[]]*n
for i in xrange(o):
	a,b,c=raw_input("").split()
	a=int(a)
	b=int(b)
	c=int(c)
	if a == 1:
		z=(b^lastans)%n
		seq=l[z]
		s=seq[:]
		s.append(c)
		l[(b^lastans)%n]=s
	elif a == 2:
		seq=(b^lastans)%n
		seq=l[seq]
		lastans=seq[c%len(seq)]
		print lastans
		
