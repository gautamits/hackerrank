def print_rangoli(size):
    # your code goes here
    arr=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    a=[]
    for i in range(1,size+1):
        string=arr[size-i:size][::-1]+arr[size-i:size][1:]
        print '-'*((size-i)*2)+'-'.join(string)+'-'*((size-i)*2)
        a.append('-'*((size-i)*2)+'-'.join(string)+'-'*((size-i)*2))
    for i in a[:-1][::-1]:
        print i
