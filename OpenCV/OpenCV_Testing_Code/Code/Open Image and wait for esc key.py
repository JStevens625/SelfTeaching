import cv2

img = cv2.imread('SampleData/aero1.jpg',1)

cv2.imshow('image', img)

x = cv2.waitKey(0)

if x == 27:
    cv2.destroyAllWindows()
