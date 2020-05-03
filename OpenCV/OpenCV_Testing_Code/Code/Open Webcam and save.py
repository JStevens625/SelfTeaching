import cv2

capture = cv2.VideoCapture(0);
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('OutputVideo.avi',fourcc, 50.0, (640,480))
#print('Frame Height: ',capture.get(cv2.CAP_PROP_FRAME_HEIGHT)) #Print Height of Window
#print('Frame Width: ',capture.get(cv2.CAP_PROP_FRAME_WIDTH)) #Print Width of Window

while(capture.isOpened()):
    ret,frame = capture.read()
    if ret == True:
        output.write(frame)
        cv2.imshow('Webcam',frame)
        if cv2.waitKey(1) == 27:
            break

capture.release()
output.release()
cv2.destroyAllWindows()
