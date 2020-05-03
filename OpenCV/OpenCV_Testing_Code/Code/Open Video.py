import cv2

capture = cv2.VideoCapture('SampleData/Megamind.avi');
while(True):
    ret,frame = capture.read()
    cv2.imshow('Webcam',frame)
    x = cv2.waitKey(1)
    if x == 27:
        break
capture.release()
cv2.destroyAllWindows()
