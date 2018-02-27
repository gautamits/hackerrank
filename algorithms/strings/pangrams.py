# Enter your code here. Read input from STDIN. Print output to STDOUT
m=[]
for i in range(1,27):
    m.append(0)
for i in input().upper():
    try:
        m[ord(i)-65]=1
    except:
        pass
if sum(m)==26:
    print('pangram')
else:
    print('not pangram')
    
