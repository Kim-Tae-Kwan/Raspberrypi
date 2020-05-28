# 라즈베리파이 카메라 얼굴 인식(Opencv)
import numpy as np
import cv2
faceCascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(3,640) # 넓이 설정
cap.set(4,480) # 높이 설정

while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame,-1) # 상하반전, 0: 좌우반전, 1: 정산, 2: 상하좌우반전
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,

        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20,20)
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y,),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h,x:x+w]

    cv2.imshow('video',frame) # video라는 이름으로 출력
    
    k = cv2.waitKey(30) & 0xff
    if k==27:  # press 'ESC' to quit ESC를 누르면 종료
        break

cap.release()
cv2.destroyAllWindows()