import numpy as np
arr=map(float,raw_input().split())
arr=np.array(arr)
print np.floor(arr)
print np.ceil(arr)
print np.rint(arr)