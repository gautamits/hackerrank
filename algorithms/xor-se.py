def a(n):
    if n==0:
        return 0
    elif n%4==1:
        return 1
    else:
        return n^a(n-1)
for _ in xrange(int(raw_input())):
    m,n=map(int,raw_input().split())
    res=0
    i=m+1
    while i < n:
        res=res^i
        i+=2
    if (n-m)%2==0:
        res=res^n^a(n-1)
    print res
