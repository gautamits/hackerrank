import numpy as np
arr1=np.array(map(int,raw_input().split()))
arr2=np.array(map(int,raw_input().split()))
print np.inner(arr1,arr2)
print np.outer(arr1,arr2)