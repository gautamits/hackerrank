t=int(raw_input())
arr=raw_input().split()
arr=[int(i) for i in arr]
day=0
arr2=sorted(arr)
if arr2==arr:
	print 1,' exiting'
	exit(0)
while True:
	#print 'day ',day
	
	labels=[]
	for i in xrange(len(arr)):
		if i > 0 and arr[i] > arr[i-1]:
			labels.append(i)
	#print labels
	if labels==[]:
		break
	i=1
	for i in xrange(len(labels)):
		c=arr.pop(labels[i])
		#print c,' popped'
		labels=[j-1 for j in labels]
					
			
	day+=1
	#print arr
print day
