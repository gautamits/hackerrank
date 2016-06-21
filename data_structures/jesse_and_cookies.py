"""def makesweet(arr,d,m):
	print d
	if arr[0]>m:
		return d
	elif len(arr)<2:
		return -1
	else:
		n=arr[0]+2*arr[1]
		arr=arr[1:]
		i=0
		while arr[i] < n:
			if i+1==len(arr): break
			arr[i]=arr[i+1]
			#print arr
			i+=1
		if i+1!=len(arr): i-=1
		arr[i]=n
		return makesweet(arr,d+1,m)
"""

l,m=raw_input().split()
l=int(l)
m=int(m)
arr=raw_input().split()
arr=[int(i) for i in arr]
arr=sorted(arr)
d=0
while arr[0] < m:
	print arr
	if len(arr) < 2:
		print -1
		exit(0)
	else:
		n=arr[0]+2*arr[1]
		arr=arr[1:]
		i=0
		while arr[i] < n:
			if i+1==len(arr): break
			arr[i]=arr[i+1]
			#print arr
			i+=1
		if i+1!=len(arr): i-=1
		arr[i]=n
	d+=1
print d

