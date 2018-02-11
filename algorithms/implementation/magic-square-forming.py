import sys
import math
def diff(a,s):
    #print a
    #print s
    ans=0;
    for i in range(3):
        for j in range(3):
            if a[i][j]!=s[i][j]:
                ans+=abs(a[i][j]-s[i][j])
    return ans
def formingMagicSquare(s):
    # Complete this function
    a=[[4,9,2],[3,5,7],[8,1,6]]
    m=diff(a,s)
    arr=[s,s[::-1],list(zip(*s)),list(zip(*s[::-1]))]
    for i in range(4):
        arr.append([j[::-1] for j in arr[i]])
    fin=[a,a[::-1],list(zip(*a)),list(zip(*a[::-1]))]
    for i in range(4):
        fin.append([j[::-1] for j in fin[i]])
    for i in arr:
        for j in fin:
            if diff(i,j) < m:
                m=diff(i,j)
    #print ans.index(min(ans))
    return m

if __name__ == "__main__":
    s = []
    for s_i in xrange(3):
        s_temp = map(int,raw_input().strip().split(' '))
        s.append(s_temp)
    result = formingMagicSquare(s)
    print result
