from tkinter import *
import pyautogui,   string
from tkinter import messagebox
import time
from PIL import Image,ImageTk
from tkinter import ttk
import sqlite3





class Reset_Password:
    def __init__(self,root):
        self.root=root
        self.root.title("Reset Password")
        self.root.geometry("450x600+650+180")
        #self.root.geometry("1550x800+0+0")
        
        self.status="No"
        self.user="None"
        self.var_pass=""
        self.var_confirmpass=""



        f_lbl=Label(self.root,height=650,width=180)
        f_lbl.place(x=10,y=10,width=650,height=180)

        frame=Frame(self.root,bg="black")
        frame.place(x=10,y=10,width=430,height=580)

        #icon
        icon=PhotoImage(file=r"Images\Icon.png")
        root.iconphoto(False,icon)

        img1=Image.open(r"Images\login.png")
        img1=img1.resize((100,100),resample=0)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(frame,image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=155,y=0,width=100,height=100)


        get_str=Label(frame,text="Reset Password",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=100,y=102)


        #======User Name Varify=====
        user=Label(frame,text=" User Name or Email",font=("times new roman",13,"bold"),fg="white",bg="black")
        user.place(x=50,y=170)

        self.Email=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.Email.place(x=45,y=202,width=270)

        #Icon
        img2=Image.open(r"images\user icon.webp")
        img2=img2.resize((30,30),resample=0)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg1=Label(frame,image=self.photoimg2,bg="black",borderwidth=0)
        lblimg1.place(x=28,y=170,width=30,height=30)

        #=====New Password====

        password=Label(frame,text=" New Password",font=("times new roman",13,"bold"),fg="white",bg="black")
        password.place(x=50,y=270)

        self.var_pass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.var_pass.place(x=45,y=302,width=270)

        #Icon
        img3=Image.open(r"Images\password.jpg")
        img3=img3.resize((30,30),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        self.photoimConfpass=ImageTk.PhotoImage(img3)


        lblimg1=Label(frame,image=self.photoimg3,bg="black",borderwidth=0)
        lblimg1.place(x=28,y=264,width=30,height=30)

        
        #=====Confirm Password=====
        confpassword=Label(frame,text=" Confirm Password",font=("times new roman",13,"bold"),fg="white",bg="black")
        confpassword.place(x=60,y=370)

        self.var_confirmpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.var_confirmpass.place(x=57,y=402,width=270)

        #Icon
        lblimg1=Label(frame,image=self.photoimConfpass,bg="black",borderwidth=0)
        lblimg1.place(x=28,y=364,width=30,height=30)


        


        # =============Reset button=============

        loginbtn=Button(frame,text="Reset",command=self.Reset,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue")
        loginbtn.place(x=140,y=460,width=120,height=35)

        #Varify Button
        varifynbtn=Button(frame,text="Varify",command=self.varify,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="green")
        varifynbtn.place(x=340,y=200,width=80,height=35)



#==========Function Declaration======
        
    #=====Varify=====
    def varify(self):
        if self.Email.get()=="":
            messagebox.showerror("Error","Please enter the Email to reset Password")
        else:
            conn=sqlite3.connect(r'User DataBase.db')
            cursor=conn.cursor()
            cursor.execute("SELECT Email FROM User")
            data_user=cursor.fetchall()
            conn.commit()
            conn.close()
            Email_user=[]
            if len(data_user)!=0:
                a=0
                for i in data_user:
                     Email_user.append(data_user[a])
                     a=a+1

                Email_user = [item[0] for item in Email_user] 

            if self.Email.get() not in Email_user:
                messagebox.showerror("Error","No Such Email or User Registered!",parent=self.root)
            else:
                self.status="Yes"
                self.user=self.Email.get()
                messagebox.showinfo("Info","User Varified",parent=self.root)



    #=====Reset====
    def Reset(self):
        if self.status=="No":
            messagebox.showwarning("Warning","Varify The Email First",parent=self.root)
        elif self.var_pass.get()=="" or self.var_confirmpass.get()=="":
            messagebox.showerror("Error","Both fields are required",parent=self.root)    
        elif len(self.var_pass.get())<6:
            messagebox.showerror("Error","Password Should Be More than 6",parent=self.root)
        elif self.var_pass.get()!=self.var_confirmpass.get():
            messagebox.showerror("Error","Password and Confirm Password must be same",parent=self.root)
        else:
            conn=sqlite3.connect(r'User DataBase.db')
            cursor=conn.cursor()
            cursor.execute("UPDATE User SET Password=? WHERE Email=?",(self.var_confirmpass.get(),self.user))
            conn.commit()
            conn.close()
            messagebox.showinfo("Info","Password Successfully Reset\nYou Can Login",parent=self.root)
            self.root.destroy()



if __name__=="__main__":
    root=Tk()
    app=Reset_Password(root)
    #login=LW()
    #print(login.Email)
    root.mainloop()

