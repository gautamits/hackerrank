def bone(n, k, b):
    if n > (k-b+1 + k) * b / 2:
        print -1
        return
    ans = [n / b for i in xrange(b)]
    for i in xrange(b/2):
        ans[i] -= b/2 - i
    for i in xrange(b/2, b):
        ans[i] += i - b/2
    diff = n - sum(ans)
    while diff > 0:
        for i in xrange(b-1,-1,-1):
            if diff == 0:
                break
            ans[i] += 1
            if ans[i] > k:
                print -1
                return
            diff -= 1
    for i in xrange(1, len(ans)):
        if ans[i] == ans[i-1]:
            print -1
            return
    print " ".join(str(e) for e in ans) if ans[0] >= 1 else -1
        
for _ in xrange(int(raw_input()):
    n,k,b = map(int, raw_input().split(' '))
    bone(n, k, b)
