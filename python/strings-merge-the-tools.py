def merge_the_tools(string, k):
    # your code goes here
    n=len(string)
    for i in range(0,n,k):
        sub=string[i:i+k]
        s=set()
        a=""
        for i in sub:
            if i in s:
                pass
            else:
                a+=i
                s.add(i)
        print a
