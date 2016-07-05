from collections import defaultdict
N,M=map(int,raw_input().split())
d=defaultdict(list)
for i in range(N):
	s=raw_input().rstrip()
	d[s].append(i+1)
for _ in range(M):
	s=raw_input().rstrip()
	if s in d:
		print(' '.join(map(str,d[s])))
	else:
		print('-1')