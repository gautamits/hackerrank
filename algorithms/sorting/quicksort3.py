def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right


def quicksort(arr,lo,hi):
	if lo < hi:
		p=partition(arr,lo,hi)
		print arr
		quicksort(arr,lo,p-1)
		quicksort(arr,p+1,hi)
		#return quicksort(arr,lo,p-1)+quicksort(arr,p+1,hi)
n=raw_input()
arr=raw_input().split()
arr=[int(i) for i in arr]
quicksort(arr,1,len(arr)-1)
print arr