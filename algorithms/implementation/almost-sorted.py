n = int(input())
arr = list(map(int,input().split()))
s = sorted(arr)
a = []
subarr = []
c = 0
for i in range(n):
    if arr[i] != s[i] :
        c += 1
        a.append(i+1)
if c == 2:
    print("yes")
    print("swap", a[0],a[1],sep = " ")
else:       
    for i in range(n):
        if arr[i] != s[i] :
            subarr.append(arr[i])
            
    if subarr == sorted(subarr)[::-1]:
        print("yes")
        print("reverse", arr.index(subarr[0])+1,arr.index(subarr[-1])+1,sep=" ")
    else:
        print("no")

