or _ in range(input()):
    big = []
    small = []
    R, C = map(int, raw_input().split())
    for __ in range(R):
        big.append(raw_input())
    r, c = map(int, raw_input().split())
    for __ in range(r):
        small.append(raw_input())
    found = False
    for i in range(R - r + 1):
        for j in range(C - c + 1):
            flag = True
            for k in range(r):
                for l in range(c):
                    if big[i + k][j + l] != small[k][l]:
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                print "YES"
                found = True
                break
        if found:
            break
    else:
        print "NO"