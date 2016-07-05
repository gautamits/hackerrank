for _ in xrange(int(raw_input())):
	money=int(raw_input())
	raw_input()
	arr=map(int,raw_input().split())
	#arr=sorted(arr)
	for i in xrange(0,len(arr)):
		j=i+1
		while j < len(arr):
			if arr[i]+arr[j]==money:
				print i+1,j+1
				break
			j+=1
