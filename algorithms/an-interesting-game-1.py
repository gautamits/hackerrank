# When we delete the max element and all elements to its right, 
# the new max element must be the max before the deleted element was
# added to the array.

for _ in range(int(raw_input())):
    N = int(raw_input())
    max_x, peaks = 0, 0
    for x in map(int, raw_input().split()):
        if x > max_x:
            max_x = x
            peaks += 1
    if peaks%2!=0:
        print 'BOB'
    else:
        print 'ANDY'
