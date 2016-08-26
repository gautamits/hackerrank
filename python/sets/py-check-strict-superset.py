s=set(map(int,raw_input().split()))
n=int(raw_input())
for _ in xrange(n):
	b=set(map(int,raw_input().split()))
	if s.intersection(b)== b and s.intersection(b) != s:
		continue
	else:
		print "False"
		exit(0)
print "True"