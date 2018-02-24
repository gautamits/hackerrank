#!/bin/python3

import sys

def gridlandMetro(n, m, k, track):
    # Complete this function
    ans=n*m
    cal={}
    for i,j,k in track:
        #print ([i,j,k])
        #print(cal,ans)
        
        if i in cal:
            prevj,prevk=cal[i]
            if prevj > j:
                ans-=(prevj-j)
                cal[i][0]=j
            if prevk < k:
                ans-=(k-prevk)
                cal[i][1]=k
        else:
            #print('reducing ',ans,' by ',abs(j-k)+1)
            ans-=abs(j-k)+1
            cal[i]=[j,k]
    return ans

if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    track = []
    for track_i in range(k):
       track_t = [int(track_temp) for track_temp in input().strip().split(' ')]
       track.append(track_t)
    result = gridlandMetro(n, m, k, track)
    print(result)