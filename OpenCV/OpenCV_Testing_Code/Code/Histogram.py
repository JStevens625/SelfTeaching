import cv2
import numpy as np
import matplotlib as mpl

img = cv2.imread('SampleData/ela_modified.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
CVhistogram = cv2.calcHist([img],[0],None,[256],[0,255])
mplhist = mpl.pyplot.hist
cv2.imshow('Image',img)
cv2.imshow('Histogram',CVhistogram)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
