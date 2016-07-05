# Enter your code here. Read input from STDIN. Print output to STDOUT
n=raw_input()
arr=map(int,raw_input().split())
for i in xrange(arr.count(max(arr))):
    arr.remove(max(arr))
print max(arr)