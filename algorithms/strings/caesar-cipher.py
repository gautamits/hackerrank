#!/bin/python3

import sys
#ascii A-Z:65-90 && a-z:97-122

n = int(input())
s = input()
k = int(input())

for i in range(len(s)):
    if 97 <= ord(s[i]) <= 122:
        s = s[:i] + chr(((ord(s[i])-97+k)%26)+97) + s[i+1:]
    elif 65 <= ord(s[i]) <= 90:
        s = s[:i] + chr(((ord(s[i])-65+k)%26)+65) + s[i+1:]

print (s)

