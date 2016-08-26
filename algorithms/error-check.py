arr=[]
arr2=[]
n=int(raw_input())
for _ in xrange(n):
	arr.append(map(int,raw_input().split()))
for _ in xrange(n):
	arr2.append(int(raw_input()))
i=0
while i < len(arr2):
	if arr2[i] != arr[i][0]:
		print i,arr2[i],arr[i]
	i+=1