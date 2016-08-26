import numpy as np
arr=np.array(map(float,raw_input().split()))
n=int(raw_input())
print np.polyval(arr,n)