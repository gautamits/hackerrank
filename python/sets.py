m=raw_input()
arr=map(int,raw_input().split())
M=set(arr)
n=raw_input()
arr=map(int,raw_input().split())
N=set(arr)
print "\n".join(map(str,sorted(list(M^N))))