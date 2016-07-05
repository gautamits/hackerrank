from operator import itemgetter
i,j=raw_input().split()
i=int(i)
j=int(j)
a=[]
for i in xrange(i):
    arr=map(int,raw_input().split())
    a.append(arr)
c=int(raw_input())

a=sorted(a,key=itemgetter(c))
for i in a:
    print " ".join(map(str,i))