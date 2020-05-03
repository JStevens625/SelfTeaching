import cv2

capture = cv2.VideoCapture(0);
while(True):
    ret,frame = capture.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Webcam',gray)

    x = cv2.waitKey(1)
    if x == 27:
        break
capture.release()
cv2.destroyAllWindows()
