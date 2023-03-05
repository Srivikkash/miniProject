# face emotion detection in live camera

import cv2
from deepface import DeepFace

face_cascade = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    
    ret,frame = cap.read()
    
    result = DeepFace.analyze(img_path= frame , actions=['emotion'], enforce_detection=False)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(frame,1.1,4)

    emotion=result[0]['dominant_emotion']
    txt = str(emotion)
    danger=['sad','fear','anger']

    for (x,y,w,h) in faces:
        if txt in danger:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        else:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    cv2.putText(frame,txt,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
