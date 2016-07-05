from collections import Counter
raw_input()
m1=Counter(map(int,raw_input().split()))
raw_input()
m2=Counter(map(int,raw_input().split()))
#print m1
#print m2
for i in m1.keys():
	if m1[i]!=m2[i]:
		print i,