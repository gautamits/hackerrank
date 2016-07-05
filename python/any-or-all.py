raw_input()
ar=raw_input().split()
print all([all([int(i)>0 for i in ar]),any([i==i[::-1] for i in ar])])