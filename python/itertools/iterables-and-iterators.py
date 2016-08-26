from itertools import combinations
raw_input()
arr=raw_input().split()
k=int(raw_input())
count=0
for i in list(combinations(arr,k)):
	if 'a' in i:
		count+=1
print float(count)/len(list(combinations(arr,k)))