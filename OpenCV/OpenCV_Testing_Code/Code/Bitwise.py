import cv2
import numpy as np

img1 = np.zeros((250,500,3),np.uint8)
img1 = cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2 = cv2.imread('SampleData/gradient.png')
#bitAnd = cv2.bitwise_and(img2,img1)
#img1 = cv2.resize(img1,)

cv2.imshow("Image",img1)
cv2.imshow("Image2",img2)
#cv2.imshow("ImageAnd",bitAnd)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
