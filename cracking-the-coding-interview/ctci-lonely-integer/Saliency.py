def Saliency(I)# I is color image
	#convert I to grayscale
	G=int((I[::0]+I[::1]+I[::2])/3)


	return numpy.array(G,np.uint8)
i=cv2.imread("lena.jpg")
cv2.imshow("saliency",i)
cv2.waitKey(0)