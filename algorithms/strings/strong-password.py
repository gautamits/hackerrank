#!/bin/python3

import sys

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    s=set()
    for i in password:
        if ord(i) in range(97,123):
            s.add('a')
        elif ord(i) in range(65,91):
            s.add('A')
        elif ord(i) in range(48,58):
            s.add('0')
        elif ord(i) in range(33,34) or ord(i) in range(35,39) or ord(i) in range(40,44) or ord(i) in range(45,46):
            s.add("@")
    #print(s,password)
    if len(s)==4 and len(password)>=6:
        return 0
    elif len(s)==4 and len(password) < 6:
        return 6-len(password)
    else:
        if 4-len(s) < 6-len(password):
            return 6-len(password)
        else:
            return 4-len(s)
        

if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    answer = minimumNumber(n, password)
    print(answer)

