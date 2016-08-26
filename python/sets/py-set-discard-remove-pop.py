raw_input()
s=set(map(int,raw_input().split()))
commands=int(raw_input())
for _ in xrange(commands):
	c=raw_input()
	if c=="pop":
		s.pop()
	else:
		c,n=c.split()
		n=int(n)
		if c=="remove":
			s.remove(n)
		else:
			s.discard(n)
print sum(s)
