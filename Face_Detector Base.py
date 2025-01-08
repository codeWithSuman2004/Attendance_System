import cv2
import numpy as np
import os
import sqlite3

facedetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(1)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("classifier.xml")

def getProfile(id):
    conn=sqlite3.connect("Face Recognizer.db")
    cursor=conn.execute("SELECT * FROM student WHERE StudentID=?", (str(id),))
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile


while(True):
    ret,img=cam.read()
    img=cv2.flip(img,1)
    img=cv2.medianBlur(img,5)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=facedetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf=recognizer.predict(gray[y:y+h,x:x+w])
        profile=getProfile(id)
        confidence = int((100*(1-conf/300)))
        if(profile != None):
            #cv2.putText(img,"To QUIT This Pocess Press 'Q'",(0,0),cv2.FONT_HERSHEY_COMPLEX,.8,(0,255,0),2)
            if confidence > 85:
                cv2.putText(img, "Name : "+str(profile[0]), (x,y-55),cv2.FONT_HERSHEY_COMPLEX, 1,(255,0,0),2)
                cv2.putText(img, "Roll : "+str(profile[2]), (x,y-30),cv2.FONT_HERSHEY_COMPLEX, 1,(255,0,0),2)
                cv2.putText(img, "Dep : "+str(profile[4]), (x,y-5),cv2.FONT_HERSHEY_COMPLEX, 1,(255,0,0),2)
                # cv2.putText(img, output_text, (50,50),cv2.FONT_HERSHEY_COMPLEX, 1,(0,255,127),2)
                
            else:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)    

    cv2.imshow("Face is Reading[To QUIT This Pocess]",img)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
