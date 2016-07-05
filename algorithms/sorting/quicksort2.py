def qsort(arr):
	if len(arr)<=1:
		return arr
	else:
		key=arr[0]
		left=[]
		right=[]
		equal=[]
		for i in arr:
			if i < key:
				left.append(i)
			elif i > key:
				right.append(i)
			else:
				equal.append(i)
		left=qsort(left)
		right=qsort(right)
		print " ".join(map(str,left+equal+right))
		return left+equal+right

n=raw_input()
ar=raw_input().split()
ar=[int(i) for i in ar]
qsort(ar)