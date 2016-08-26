n=raw_input()
arr=raw_input().split()
arr=[int(i) for i in arr]
index=1
shifts=0
while index < len(arr):
	element=arr[index]
	j=index
	while element < arr[j-1] and j >=1:
		arr[j]=arr[j-1]
		shifts+=1
		j-=1
	arr[j]=element
	index+=1
	
print shifts