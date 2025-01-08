from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from PIL import Image,ImageTk
import os
from Student import Student
import Face_Recongnizer
import Train_Data
from help import Help
from developer import Developer
from Attendance import Attendance
from Get_Subscription import Payment
import Check_Subscription


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #Icon
        icon=PhotoImage(file=r"Images\icon.png")
        root.iconphoto(False,icon)


        #---first image---
        img1=Image.open(r"Images\bg.jpg")
        img1=img1.resize((500,150),resample=0)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=150)

        #-----second image-----
        img2=Image.open(r"Images\bg1.jpg")
        img2=img2.resize((500,150))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=550,height=150)

        #-----third image-----
        img3=Image.open(r"Images\bg3.jpg")
        img3=img3.resize((500,150))
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=550,height=150)

        #-----background image-----
        img4=Image.open(r"Images\bg5.jpg")
        img4=img4.resize((1530,790))
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=150,width=1530,height=790)

        #-----title-----
        title_lbl=Label(bg_img,text="FACE  RECOGNITION  ATTENDANCE  SOFTWARE",font=("times new roman",35,"bold","italic"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #-----student button-----
        img5=Image.open(r"Images\student-details.jpg")
        img5=img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.Student_details,cursor="hand2")
        b1.place(x=200,y=70,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.Student_details,cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="blue")
        b1_1.place(x=200,y=270,width=220,height=40)

        #-----detect face button-----
        img6=Image.open(r"Images\face1.jpg")
        img6=img6.resize((220,220))
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,command=self.Face_detector,cursor="hand2")
        b1.place(x=500,y=70,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",command=self.Face_detector,cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="blue")
        b1_1.place(x=500,y=270,width=220,height=40)

        #-----attendance button-----
        img7=Image.open(r"Images\attendance.jpg")
        img7=img7.resize((220,220))
        self.photoimg7=ImageTk.PhotoImage(img7)
        b1=Button(bg_img,image=self.photoimg7,command=self.Attendance,cursor="hand2")
        b1.place(x=800,y=70,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",command=self.Attendance,cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="blue")
        b1_1.place(x=800,y=270,width=220,height=40)

        #-----help desk button-----
        img8=Image.open(r"Images\help.jpg")
        img8=img8.resize((220,220))
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,command=self.Help,cursor="hand2")
        b1.place(x=1100,y=70,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",command=self.Help,cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="blue")
        b1_1.place(x=1100,y=270,width=220,height=40)

        #-----train face button-----
        img9=Image.open(r"Images\train.jpg")
        img9=img9.resize((220,220))
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,command=self.Train_Data,cursor="hand2")
        b1.place(x=200,y=350,width=220,height=220)

        b1_1=Button(bg_img,text="Train Faces",command=self.Train_Data,cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="blue")
        b1_1.place(x=200,y=550,width=220,height=40)

        #-----photos button-----
        img10=Image.open(r"Images\photo.jpg")
        img10=img10.resize((220,220))
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,command=self.open_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=500,y=350,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",command=self.open_img,cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="blue")
        b1_1.place(x=500,y=550,width=220,height=40)
        

        #-----Developer button-----
        Developer=Image.open(r"Images\Developer.jpg")
        Developer=Developer.resize((220,220))
        self.DeveloperIMG=ImageTk.PhotoImage(Developer)

        Developer_Button=Button(bg_img,image=self.DeveloperIMG,command=self.Developer,cursor="hand2")
        Developer_Button.place(x=800,y=350,width=220,height=220)

        Developer_Button_Text=Button(bg_img,text="Developers",command=self.Developer,cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="blue")
        Developer_Button_Text.place(x=800,y=550,width=220,height=40)

        #-----exit button-----
        img12=Image.open(r"Images\exit.jpg")
        img12=img12.resize((220,220))
        self.photoimg12=ImageTk.PhotoImage(img12)

        Exit_Button=Button(bg_img,image=self.photoimg12,command=self.Exit,cursor="hand2")
        Exit_Button.place(x=1100,y=350,width=220,height=220)

        Exit_Button_Text=Button(bg_img,text="Exit",command=self.Exit,cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="blue")
        Exit_Button_Text.place(x=1100,y=550,width=220,height=40)


        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?",parent=self.root):
                #self.root.destroy()
                exit(0)

        self.root.protocol("WM_DELETE_WINDOW", on_closing)  


    #======Function Buttons======
    def Student_details(self):
        #self.root.withdraw()
        if Check_Subscription.Check_Subscription():
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)
        else:
            Subs=messagebox.askyesno("Warning","Your Subscription is Expired\nYou Can't Access our services\n\nDo you Want To Buy A subscription?",parent=self.root)
            if Subs >0:
                self.new_window=Toplevel(self.root)
                self.app=Payment(self.new_window)
            else:
                if not Subs:
                    return    



    def Face_detector(self):
            if Check_Subscription.Check_Subscription():
                messagebox.showinfo("Success","Face Detector Is Being Ready,Please Wait",parent=self.root)
                Face_Recongnizer.face_recognition()
                #self.new_window=Toplevel(self.root)
            else:
                Subs=messagebox.askyesno("Warning","Your Subscription is Expired\nYou Can't Access our services\n\nDo you Want To Buy A subscription?",parent=self.root)
                if Subs >0:
                    self.new_window=Toplevel(self.root)
                    self.app=Payment(self.new_window)
                else:
                    if not Subs:
                        return    #self.app=Face_Recognition(self.new_window)



    def Train_Data(self):
                messagebox.showinfo("Info","Please Wait to Process the Data\nWhen Traing Will be completed you will get a message",parent=self.root)
                #self.new_window=Toplevel(self.root)
                #self.app=Train_Data(self.new_window)
                self.root.withdraw()
                Train_Data.train_classifier()
                self.root.deiconify()
                messagebox.showinfo("Success","Training data set completed",parent=self.root)

    def Help(self):
                #self.root.withdraw()
                self.new_window=Toplevel(self.root)
                self.app=Help(self.new_window)


    def Developer(self):
                #self.root.withdraw()
                self.new_window=Toplevel(self.root)
                self.app=Developer(self.new_window) 
                     

       

    def Attendance(self):
                if Check_Subscription.Check_Subscription():
                    #self.root.withdraw()
                    self.new_window=Toplevel(self.root)
                    self.app=Attendance(self.new_window)
                else:
                    Subs=messagebox.askyesno("Warning","Your Subscription is Expired\nYou Can't Access our services\n\nDo you Want To Buy A subscription?",parent=self.root)
                    if Subs >0:
                        self.new_window=Toplevel(self.root)
                        self.app=Payment(self.new_window)
                    else:
                        if not Subs:
                            return  

    def open_img(self):
        os.startfile("Data")
                               

    def Exit(self):
            if messagebox.askokcancel("Quit", "Do you want to Exit?"):
                exit(0)        



if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

        
