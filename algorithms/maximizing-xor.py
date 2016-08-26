def maximize(l,r):
  a=[i^j for i in xrange(l,r+1) for j in xrange(i,r+1)]
  return a
l=int(raw_input())
r=int(raw_input())
print maximize(l,r)