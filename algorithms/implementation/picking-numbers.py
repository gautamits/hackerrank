#!/bin/python
raw_input()
a = map(int,raw_input().split())
print max(a.count(x)+a.count(x+1) for x in set(a))