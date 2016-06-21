import sys
import cv2
import numpy as np
n=len(sys.argv)-1
print n,'images'
i=1
images=[]
index=np.arange(n)
index=480*index
while i<=n:
	images.append(cv2.resize(cv2.imread(sys.argv[i],1),(640,480)))
	i+=1
stitched=np.empty((480*n,640,3))
j=0
for i in index:
	stitched[i:480+i,:]=images[j]
	j+=1
print "stitched"
cv2.imwrite("final.jpg",stitched)


