import cv2
import sys
import numpy as np
path=sys.argv[1]
image=cv2.imread(path,1)
right=np.pad(image,((1,1),(0,0)))
