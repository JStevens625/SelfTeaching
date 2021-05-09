import cv2
import numpy as np

img = cv2.imread('../SampleData/aero1.jpg',1)
line = cv2.line(img,(0,0),(255,255),(0,0,255),10)
arrow1 = cv2.arrowedLine(img,(0,255),(255,255),(255,0,0),10)
rec = cv2.rectangle(img,(50,50),(100,300),(0,255,0),-1)

while True:
    cv2.imshow('Canvas',img)
    x = cv2.waitKey(0)
    if x == 27:
        break
cv2.destroyAllWindows()
