#!/usr/bin/py
def lonelyinteger(a):
    answer = a[0]
    for i in xrange(1,len(a)):
        answer=answer^a[i]
    return answer
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)