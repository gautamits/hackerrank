import numpy as np
arr=map(float,raw_input().split())
arr=np.array(arr)
print np.fliplr(np.atleast_2d(arr))[0]