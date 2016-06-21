import cv2
import numpy as np
i=0
j=0
k=0
a=0
b=0
row=[]
final=[]
column=[]
while a< 255:
	k=0
	i=0
	b=0
	while b < 255:
		row.append(i)
		row.append(j)
		row.append(k)
		column.append(row)
		i+=1
		k+=1
		b+=1
		row=[]
	j+=1
	a+=1
	final.append(column)
	column=[]
final=np.array(final)
final=np.array(final,dtype=np.uint8)
print final
print final.shape
cv2.imshow("final",final)
cv2.waitKey(0)
