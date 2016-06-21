#this prints sum of hourglass with maximum value, array size is 6x6
def getsum(patch):
	total=sum([sum(i) for i in patch])
	total=total-patch[1][0]
	total=total-patch[1][2]
	return total
def getpatch(p,a):
	i,j=p
	p=[]
	patch=a[i:i+3]
	for k in patch:
		p.append(k[j:j+3])
	return p
	
a=[]
for i in xrange(6):
	b=raw_input("").split()
	b=[int(j) for j in b]
	a.append(b)
#print a
arr=[]
for i in xrange(4):
	for j in xrange(4):
		index=(i,j)
		#print index
		patch=getpatch(index,a)
		#print patch
		total=getsum(patch)
		arr.append(total)
print max(arr)
