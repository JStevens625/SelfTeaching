import cv2
video = cv2.VideoCapture(0)
while(True):
    ret,frame = video.read()
    cv2.imshow("Webcam",frame)
    if(cv2.waitKey(1) == 27):
        cv2.destroyAllWindows()
        break
