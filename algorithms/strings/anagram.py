import sys

def anagram(s):
    # Complete this function
    if len(s)%2==1:
        return -1
    p=s[:len(s)//2]
    q=s[len(s)//2:]
    b={}
    for i in q:
        try:
            b[i]+=1
        except:
            b[i]=1
    s=0
    a={}
    for i in p:
        try:
            a[i]+=1
        except:
            a[i]=1
    for i in b:
        try:
            if b[i] > a[i]:
                s+=(b[i]-a[i])
        except:
            s+=b[i]
    
    return s

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = anagram(s)
    print(result)

