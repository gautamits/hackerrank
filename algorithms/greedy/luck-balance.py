import sys

def luckBalance(n, k, contests):
    # Complete this function
    important=[]
    s=0
    for [i,j] in contests:
        if j==1:
            important.append(i)
        else:
            s+=i
    important=sorted(important)[::-1]
    j=0
    for i in important:
        if j<k:
            s+=i
        else:
            s-=i
        j+=1
            
    return s
    

if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    contests = []
    for contests_i in xrange(n):
        contests_temp = map(int,raw_input().strip().split(' '))
        contests.append(contests_temp)
    result = luckBalance(n, k, contests)
    print result