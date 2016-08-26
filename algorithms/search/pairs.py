m,n=map(int,raw_input().split())
arr=map(int,raw_input().split())
arr=sorted(arr)
print len(arr)
#print arr
pairs=0
i=0
while i < m-2:
  #print i
  j=i+1
  while j < m-2:
    #print j,
    if arr[j]-arr[i]==n:
      pairs+=1
      break
    elif arr[j]-arr[i]>n:
      break
    else:
      j+=1
  i+=1
print pairs

