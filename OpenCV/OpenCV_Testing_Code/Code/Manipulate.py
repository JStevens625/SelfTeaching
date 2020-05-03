import cv2
import numpy as np

img = cv2.imread('SampleData/chicky_512.png')

print(img.shape) #returns tuple of number of rows, columns, channels
print(img.size) # returns Total number of pixels accessed
print(img.dtype) # returns image data type that is obtained
b,g,r = cv2.split(img) # gives BGR channels of image
img = cv2.merge((b,g,r)) # merges BGR channels

coordinates = img[300:400, 350:450]
img[100:200, 200:300] = coordinates

cv2.imshow('image',img)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
