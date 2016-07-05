from itertools import combinations
for _ in xrange(int(raw_input())):
	n,m=map(int,raw_input().split())
	arr=map(int,raw_input().split())
	res=[]
	for i in xrange(1,n):
		for j in list(combinations(arr,i)):
			res.append(j)
	#print res
	res1=[]
	for i in res:
		res1.append(sum(i)%m)
	print max(res1)
