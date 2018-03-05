#!/bin/python3

import sys

def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    money=list(range(p,m,-d))+[m]*s
    su=0
    c=0
    for i in money:
        su+=i
        if su<=s:
            c+=1
        else:
            break

    return c
if __name__ == "__main__":
    p, d, m, s = input().strip().split(' ')
    p, d, m, s = [int(p), int(d), int(m), int(s)]
    answer = howManyGames(p, d, m, s)
    print(answer)
