# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
ans=OrderedDict()
for _ in range(int(input())):
    
    q=input().split(" ")
    item=" ".join(q[:-1])
    quantity=int(q[-1])
    if item in ans:
        ans[item]=ans[item]+quantity
    else:
        ans[item]=quantity
for i in ans:
    print(i,ans[i])
