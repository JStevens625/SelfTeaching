import cv2
import numpy as np

img = [[0,255,0,0,0,255,0,255,255,255],
       [0,255,0,0,0,255,0,255,255,255],
       [0,255,0,0,0,255,0,255,255,255],
       [0,255,0,0,0,255,0,255,255,255],
       [0,255,0,0,0,255,0,255,255,255]]

gen = np.array(img ,dtype=np.uint8)

print(gen.shape)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
