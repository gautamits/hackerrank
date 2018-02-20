import itertools
n,m = map(int,input().split())
arr=[]
for i in range(n):
    arr.append(int(input(),2))
ma = -float('inf')
teams=0
for p1,p2 in itertools.combinations(range(n),2):
    combined_topics = bin(arr[p1]|arr[p2]).count('1')
    if (combined_topics==ma):
        teams+=1
    elif (combined_topics>ma):
        ma = combined_topics
        teams=1

print(ma,teams,sep='\n')

