import cv2

capture = cv2.VideoCapture(0);

while(capture.isOpened()):
    ret,frame = capture.read()
    if ret == True:
        font = cv2.FONT_ITALIC
        text = "Width: " + str(capture.get(3)) + 'Height: ' + str(capture.get(4))
        cv2.putText(frame, text, (10,50),font, 1, (0,255,255), 2, cv2.LINE_AA)
        cv2.imshow('Webcam',frame)

    x = cv2.waitKey(1)
    if x == 27:
        break

capture.release()
cv2.destroyAllWindows()
