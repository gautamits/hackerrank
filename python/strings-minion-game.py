def minion_game(string):
    # your code goes here
    string=string.lower()
    stuart=0
    kevin=0
    n=len(string)
    for i in range(len(string)):
        s=n-i
        if string[i]=='a' or string[i]=='e' or string[i]=='i' or 
string[i]=='o' or string[i]=='u':
            kevin+=s
        else:
            stuart+=s
        #print i,stuart,kevin
    if stuart>kevin:
        print "Stuart",stuart
    elif kevin>stuart:
        print "Kevin",kevin
    else:
        print "Draw"
