from itertools import product
a=[]
a.append(map(int,raw_input().split()))
a.append(map(int,raw_input().split()))
print " ".join(map(str,list(product(*a))))