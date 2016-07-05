a=[0]*61
a[0]=1
i=0
while i <= 60:
	a[i]=a[i-2]*2+1
	i+=2
i=1
while i <= 60:
	a[i]=a[i-1]*2
	i+=2
t=int(raw_input())
while t > 0:
	j=int(raw_input())
	print a[j]
	t-=1


