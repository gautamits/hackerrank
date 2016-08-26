s=raw_input()
arr=raw_input().split()
arr=[int(i) for i in arr]
element=arr[len(arr)-1]
index=len(arr)-1
while index>=1 and arr[index-1]> element:
	arr[index]=arr[index-1]
	index-=1
	for i in arr:
		print i,
	print ""
arr[index]=element
for i in arr:
		print i,
