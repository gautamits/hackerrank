def getClosestSmaller(x):
    x |= x >> 1
    x |= x >> 2
    x |= x >> 4
    x |= x >> 8
    x |= x >> 16
    x |= x >> 32
    x = x + 1
    x = x >> 1
    return x

def Reductions(x):
    reductions = 1

    while (x != 1):
        #print x
        if x & (x - 1):
            #print "x is not power of two"
            x -= getClosestSmaller(x)
        else:
            #print "x is power of two"
            x /= 2
        reductions += 1

    return reductions

if __name__ == '__main__':
    t = input()
    for _ in xrange(t):
        n = input()
        if Reductions(n) % 2 != 0:
            print "Richard"
        else:
            print "Louise"
