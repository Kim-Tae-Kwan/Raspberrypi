import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(3,480)
cap.set(4,320)
mog = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    ret,frame = cap.read()
    fgmask = mog.apply(frame)

    cv2.imshow('MOG',fgmask)
    cv2.imshow('MOG2',frame)
    k=cv2.waitKey(1)&0xFF
    if k== 27:
        break

cap.release()
cv2.destroyAllWindows()