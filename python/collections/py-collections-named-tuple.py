n=int(input())
t=__import__('collections').namedtuple('t',input().split())
a=[t(*input().split()) for _ in range(n)]
print(sum(float(e.MARKS) for e in a)/n)