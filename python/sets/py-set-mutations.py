raw_input()
s=set(map(int,raw_input().split()))
for _ in xrange(int(raw_input())):
	c=raw_input().split()[0]
	if c=="intersection_update":
		s.intersection_update(set(map(int,raw_input().split())))
	elif c== "symmetric_difference":
		s.symmetric_difference(set(map(int,raw_input().split())))
	elif c=="update":
		s.update(set(map(int,raw_input().split())))
	elif c=="difference_update":
		s.difference_update(set(map(int,raw_input().split())))
	elif c=="symmetric_difference_update":
		s.symmetric_difference_update(set(map(int,raw_input().split())))

print sum(s)