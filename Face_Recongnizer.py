from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import cv2
import os
from win32com.client import Dispatch
import numpy as np
import string
from time import strftime
import time
from datetime import datetime



#===========Attendance========
def mark_attendance(ID,Roll,Name,Dept):
    with open("attendance.csv","r+",newline="\n") as f:
        myDataList=f.readlines()
        ID_list=[]
        ID_Date={}
        now=datetime.now()
        a=-1
        for line in myDataList:
            entry=line.split(",")
            if entry[0]!='\n':
                ID_list.append(entry[0])
                data=[item.split(',') for item in entry]
                if len(data)>5:
                    a=a+1
                    for i in data:
                        #if data[5][0] not in Date_list:
                            #Date_list.append(data[5][0])
                            ID_Date[ID_list[a]]=data[5][0]  
        Date=now.strftime("%d/%m/%y")
        Time=now.strftime("%H:%M:%S")
        if ID not in ID_list:
            f.writelines(f"\n{ID},{Roll},{Name},{Dept},{Time},{Date},present")
            #speak(f"{Name},YOUR ATTENDANCE SUCCESSFULLY CREATED")
        else:
            if((ID_Date[ID]!=Date)): #'''and (ID not in ID_list)'''
                f.writelines(f"\n{ID},{Roll},{Name},{Dept},{Time},{Date},present")
                #speak(f"{Name},YOUR ATTENDANCE SUCCESSFULLY CREATED")
            else:
                return 1
            
    # ========== face recognition ============#
def face_recognition():
    
    try:
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
                    if confidence > 93:
                        cv2.putText(img, "Name : "+str(profile[0]), (x,y-55),cv2.FONT_HERSHEY_COMPLEX, 1,(0,255,127),2)
                        cv2.putText(img, "Roll : "+str(profile[2]), (x,y-30),cv2.FONT_HERSHEY_COMPLEX, 1,(0,255,127),2)
                        cv2.putText(img, "Dep : "+str(profile[4]), (x,y-5),cv2.FONT_HERSHEY_COMPLEX, 1,(0,255,127),2)
                        if(mark_attendance(str(profile[1]),str(profile[2]),str(profile[0]),str(profile[4]))):
                            cv2.putText(img, "Status : "+"Attended", (x,y+h+20),cv2.FONT_HERSHEY_COMPLEX, 1,(255,255,255),2)
                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                        cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
            cv2.imshow("Face is Reading To QUIT Press Q",img)
            if cv2.waitKey(1)==ord('q'):
                break
        cam.release()
        cv2.destroyAllWindows()
    except Exception as es:
        messagebox.showerror("Error",f"Due To :{str(es)}")      
    
if __name__== "__main__":
    face_recognition()