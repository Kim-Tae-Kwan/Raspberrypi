# 라즈베리파이 얼굴 인식 데이터 수집
import os
import cv2

Face_detector = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)
cap.set(3,640) # 넓이 설정
cap.set(4,480) # 높이 설정

# 각 얼굴에 대해서 번호를 입력
face_id = input('\n enter user id end press <return>==>')
print('\n [INFO] Initalizing face capture. Look the camera and wait...')
# 개인 샘플링 얼굴 카운트 초기화
count=0

while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame,1) # 상하반전, 0: 좌우반전, 1: 정산, 2: 상하좌우반전
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = Face_detector.detectMultiScale(gray,1.3,3)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y,),(x+w,y+h),(255,0,0),2)
        count+=1
        
        cv2.imwrite("dataset/User."+ str(face_id)+'.'+str(count)+'.jpg',gray[y:y+h,x:x+w])


    cv2.imshow('image',frame) # video라는 이름으로 출력
    
    k = cv2.waitKey(100) & 0xff
    if k==27:  # press 'ESC' to quit ESC를 누르면 종료
        break
    elif count >=30:
        break

print('\n [INFO] Exiting Program and cleanup stuff')
cap.release()
cv2.destroyAllWindows()