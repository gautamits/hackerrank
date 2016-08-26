from collections import Counter
raw_input()
items=map(int,raw_input().split())
m=Counter(items)
#print m
money=0
q=int(raw_input())
for _ in xrange(q):
	a,b=map(int,raw_input().split())
	if a in m.keys():
		m[a]=m[a]-1
		if m[a]==0:
			m.pop(a,None)
		money+=b
		#print b, 'added'
	#print m
print money

