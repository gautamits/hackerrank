# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(raw_input(""))
m={}
m['(']=')'
m['{']='}'
m['[']=']'
while t>0:
    a=raw_input("")
    b=[]
    for i in a:
        if i=='(' or i=='{' or i=='[':
            b.append(i)
        elif i==')' or i=='}' or i==']':
            c=b.pop()
            if i!=m[c]:
                print 'NO'
                break
    if i==a[len(a)-1]:
        print 'YES'
    t-=1
