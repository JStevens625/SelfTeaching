import cv2

video = cv2.VideoCapture(0)

while(True):
   ret,frame = video.read()
   frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   #cv2.imshow("WebCam",frame)
   cv2.imshow("X Axis", cv2.Sobel(frame, -1, 1, 0, ksize=3))
   cv2.imshow("Y Axis", cv2.Sobel(frame, -1, 0, 1, ksize=3))
   if(cv2.waitKey(1) == 27):
        cv2.destroyAllWindows()
        break
