import numpy as np
import cv2 as cv


# 얼굴과 눈을 검출하기 위해 미리 학습시켜 놓은 XML 포맷으로 저장된 분류기를 로드합니다. 
face_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_fullbody.xml')

# 얼굴과 눈을 검출할 그레이스케일 이미지를 준비해놓습니다. 
img = cv.imread('./dataset/capture2.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# 이미지에서 얼굴을 검출합니다. 
faces = face_cascade.detectMultiScale(gray, 1.3, 5)


# 얼굴이 검출되었다면 얼굴 위치에 대한 좌표 정보를 리턴받습니다. 
for (x,y,w,h) in faces:

    # 원본 이미지에 얼굴의 위치를 표시합니다. 
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
  


# 얼굴과 눈 검출 결과를 화면에 보여줍니다.
cv.imshow('img',img)
cv.waitKey(0)

cv.destroyAllWindows()