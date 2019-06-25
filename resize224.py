import cv2
import numpy as np
import os
import io
import sys
import glob

path1='/home/konsultera/data_i3d/rgb'

lst=[]
for path, subdirs, files in os.walk(path1):
	lst.append(path)

# print(len(lst))

lst.pop(0)
# print(lst)
flst=[]
for i in lst:
	fullpath=i+'/*.jpg'
	flst.append(fullpath)

# print(flst)

ilst=[]
for i in flst:
	for filename in glob.glob(i):
		ilst.append(filename)

# print(len(ilst))

for image in ilst:
	img = cv2.imread(image, cv2.IMREAD_UNCHANGED)
	print(image)
	print('Original Dimensions : ',img.shape)
	 
	width = 224
	height = 224
	dim = (width, height)
	 
	# resize image
	img=cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	print('Resized Dimensions : ',img.shape)
	# print('Resized Dimensions : ',resized.shape)
	cv2.imwrite(image,img)
	# cv2.imshow("Resized image", resized)
	cv2.waitKey(0)
	cv2.destroyAllWindows()