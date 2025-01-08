from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import getmac
import uuid
from time import strftime
import time
import re
import email_validator
from datetime import datetime,timedelta
from main import Face_Recognition_System
from Get_Subscription import Payment



def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()


class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
      
        self.root.geometry("1550x800+0+0")

        self.textuser=StringVar()
        self.textpass=StringVar()

       #Icon
        icon=PhotoImage(file=r"Images\icon.png")
        root.iconphoto(False,icon)


        #---background image---
        img=Image.open(r"Images\bg.jpeg")
        img=img.resize((1920,1080),resample=0)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1920,height=1080)

        # ===========================
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)


        img1=Image.open(r"Images\login.png")
        img1=img1.resize((100,100),resample=0)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(frame,image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=120,y=1,width=100,height=100)


        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        # username label

        username=Label(frame,text="Username / Email",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,textvariable=self.textuser,font=("times new roman",15,"bold"))
        self.txtuser.place(x=42,y=185,width=270)

        # password label

        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,textvariable=self.textpass,font=("times new roman",15,"bold"))

        def hide(event):
            self.txtpass.config(show="*")
        self.txtpass.bind("<KeyRelease>",hide) 

        self.txtpass.place(x=42,y=260,width=270)

        # ================= Icon image==============

        img2=Image.open(r"Images\user icon.webp")
        img2=img2.resize((30,30),resample=0)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg1=Label(frame,image=self.photoimg2,bg="black",borderwidth=0)
        lblimg1.place(x=40,y=150,width=30,height=30)

        # ===============password icon===========

        img3=Image.open(r"Images\password.jpg")
        img3=img3.resize((30,30),resample=0)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg1=Label(frame,image=self.photoimg3,bg="black",borderwidth=0)
        lblimg1.place(x=40,y=224,width=30,height=30)

        # =============login button=============

        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red")
        loginbtn.place(x=110,y=305,width=120,height=35)

        # =============register button=============

        registerbtn=Button(frame,command=self.Check_Device,text="New User Register",font=("times new roman",11,"bold","italic"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=20,y=360,width=160)

        # =========forgot password button=========

        forgotbtn=Button(frame,command=self.forgotpass_window,text="Forgot Password",font=("times new roman",11,"bold","italic"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotbtn.place(x=13,y=390,width=160)

        

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?",parent=self.root):
                self.root.destroy()
                exit(0)

        self.root.protocol("WM_DELETE_WINDOW", on_closing)         

    

#============Function Declaration=======
        
      

    #======Check Subscription=======
    def Check_Subscription(self):
        try:
            MAC=getmac.get_mac_address()
            conn=sqlite3.connect(r'C:\ProgramData\Windows Secret Data.db')
            cursor=conn.cursor()
            cursor.execute("SELECT Subscription,Till_Date FROM devicemac WHERE MAC=?",(MAC,))
            Subs_Data=cursor.fetchall()
            a=0
            Subs_Detail=[]
            for i in Subs_Data:
                 Subs_Detail.append(Subs_Data[a])
                 a=a+1      

            Subs_Detail = [item for sublist in Subs_Detail for item in sublist]
            Current_Date=datetime.now()
            
            if datetime.strptime(Subs_Detail[1], '%Y-%m-%d %H:%M:%S.%f') <= Current_Date:
                #messagebox.showwarning("Warning",f"Your {Subs_Detail[0]} Is Expired")
                Subs=messagebox.askyesno("Warning",f"Your {Subs_Detail[0]} Is Expired\n Do you Want To Buy A subscription?",parent=self.root)
                if Subs >0:
                    self.new_window=Toplevel(self.root)
                    self.app=Payment(self.new_window)
                else:
                    if not Subs:
                        return     

            else:
                self.main_window()
        except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    



    #=======Check Device======
    def Check_Device(self):
        try:

            conn=sqlite3.connect(r'C:\ProgramData\Windows Secret Data.db')
            cursor=conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS devicemac(
                                           MAC TEXT, Email TEXT PRIMARY KEY,Subscription TEXT NOT NULL,
                                           Register_Date NOT NULL,
                                           Till_Date TEXT)''')

            cursor.execute("SELECT MAC FROM devicemac")
            data_mac=cursor.fetchall()
            mac_address=[]
            MAC=getmac.get_mac_address()

            a=0
            for i in data_mac:
                 mac_address.append(data_mac[a])
                 a=a+1

            mac_address = [item[0] for item in data_mac] 
            MAC="NULL"
            if MAC in mac_address:
                messagebox.showinfo("Info","This device Already Rgisterd!!\nDon't Remember Password?\nClick on Forgot Password")
                conn.commit()
                conn.close()
            else:
                self.register_window()  
        except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    
    #======Login Function=====
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=sqlite3.connect('User DataBase.db')
                cursor=conn.cursor()
                cursor.execute("SELECT Password FROM User WHERE Email=?",(self.txtuser.get(),))
                Password_Data=cursor.fetchall()
                Password=[]
                if len(Password_Data)!=0:
                    a=0
                    for i in Password_Data:
                         Password.append(Password_Data[a])
                         a=a+1

                    Password = [item[0] for item in Password]
                else:
                    Password.append("None")
                

                if self.txtpass.get()== Password[0]:
                    messagebox.showinfo("Success","Welcome,you are now logged in",parent=self.root)
                    self.textuser.set(""),
                    self.textpass.set("")
                    self.Check_Subscription()
                else:
                    messagebox.showerror("Invalid","Invalid username or password",parent=self.root)
            except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)




    #=======Forgot Password=====
    def forgotpass_window(self): 
            #self.root.withdraw()  
            self.new_window=Toplevel(self.root)
            self.app=Reset_Password(self.new_window) 

    #=======Main Window====
    def main_window(self):
        self.root.withdraw()
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition_System(self.new_window)         
        


    #======Register=====
    def register_window(self):
        #self.root.withdraw()
        self.new_window=Toplevel(self.root)
        self.app=register(self.new_window)


class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")


        #Icon
        icon=PhotoImage(file=r"Images\icon.png")
        root.iconphoto(False,icon)

        # variables--------------------------------

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_question=StringVar()
        self.var_answer=StringVar()
        self.var_pass=StringVar()
        self.var_confirmpass=StringVar()


        #---background image---
        img=Image.open(r"Images\bg1.jpg")
        img=img.resize((1530,790),resample=0)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=790)


        #---------------main frame-------------

        frame=Frame(self.root,bg="black")
        frame.place(x=500,y=100,width=675,height=550)

        register_lbl=Label(frame,text="REGISTER  HERE",font=("times new roman",20,"bold","italic"),fg="cyan",bg="black")
        register_lbl.place(x=220,y=20)


        #------------label and entry ------------

        # first name---------------

        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="black",fg="yellow")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))

        def checkName(event):
             if re.search(r"\d",self.var_fname.get()) or re.search(r"[^a-zA-Z0-9]",self.var_fname.get()) or re.search(r"\d",self.var_lname.get()) or re.search(r"[^a-zA-Z0-9]",self.var_lname.get()):
                messagebox.showerror("Error","Name Should Not Contain Any Numeric or Special Symbol!",parent=self.root)

        fname_entry.bind("<KeyRelease>",checkName)

        fname_entry.place(x=50,y=130,width=250)

        # last name------------

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="black",fg="yellow")
        lname.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))

        self.txt_lname.bind("<KeyRelease>",checkName)

        self.txt_lname.place(x=370,y=130,width=250)

        # contact-----------------

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="black",fg="yellow")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))

        def Phone_check(event):
             if self.var_contact.get()!="":
                try:
                     int(self.var_contact.get())
                except:
                     messagebox.showerror("Error","Phone No should be integer",parent=self.root)    
        self.txt_contact.bind("<KeyRelease>", Phone_check)

        self.txt_contact.place(x=50,y=200,width=250)

        # email--------------------
        
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="black",fg="yellow")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        # security question-------------

        question=Label(frame,text="Security Question",font=("times new roman",15,"bold"),bg="black",fg="yellow")
        question.place(x=50,y=240)

        self.combo_question=ttk.Combobox(frame,textvariable=self.var_question,font=("times new roman",15,"bold"),state="readonly")
        self.combo_question["values"]=("Select","Your D.O.B","Your Birth Place","Your Pet Name")
        self.combo_question.place(x=50,y=270,width=250)
        self.combo_question.current(0)

        #security answer------------------

        answer=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="black",fg="yellow")
        answer.place(x=370,y=240)

        self.txt_answer=ttk.Entry(frame,textvariable=self.var_answer,font=("times new roman",15))
        self.txt_answer.place(x=370,y=270,width=250)

        # password-----------------

        password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="black",fg="yellow")
        password.place(x=50,y=310)

        self.password=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))

        def hide(event):
            self.password.config(show="*")
        self.password.bind("<KeyRelease>",hide) 

        self.password.place(x=50,y=340,width=250)

        # confirm password--------------------

        confirm=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="black",fg="yellow")
        confirm.place(x=370,y=310)

        self.confirm=ttk.Entry(frame,textvariable=self.var_confirmpass,font=("times new roman",15))

        def hide(event):
            self.confirm.config(show="*")
        self.confirm.bind("<KeyRelease>",hide) 

        self.confirm.place(x=370,y=340,width=250)

        # check button----------------------
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I have read,understand and agree with the TERMS & CONDITIONS.",font=("times new roman",13,"bold"),bg="black",fg="red",onvalue=1,offvalue=0)
        checkbtn.place(x=65,y=400)

        # register button--------------

        img1=Image.open(r"Images\register.jpg")
        img1=img1.resize((200,55),resample=0)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimg1,command=self.register,borderwidth=0,cursor="hand2",font=("times new roman",13,"bold"),bg="black",fg="white",activebackground="black")
        b1.place(x=70,y=450,width=200)

        # login button---------------

        img2=Image.open(r"Images\log in.png")
        img2=img2.resize((180,45),resample=0)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(frame,command=self.return_login,image=self.photoimg2,borderwidth=0,cursor="hand2",font=("times new roman",13,"bold"),bg="black",fg="white",activebackground="black")
        b1.place(x=390,y=455,width=200)

        """
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.root.destroy()
                exit(0)

        self.root.protocol("WM_DELETE_WINDOW", on_closing)
        """

        
#=========function declaration========
        
    #======Rgister=====
    def register(self):
        try:
            Email=self.var_email.get()
            if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_email.get()=="" or self.var_contact.get()=="" or self.var_question.get()=="Select" or self.var_answer.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            elif len(self.var_pass.get())<6:
                messagebox.showerror("Error","Password Should Be More than 6 Charecter",parent=self.root)
            elif self.var_pass.get()!=self.var_confirmpass.get():
                messagebox.showerror("Error","Password and Confirm Password must be same",parent=self.root)
            elif self.var_check.get()==0:
                messagebox.showerror("Error","Please agree our Terms and Conditions",parent=self.root)

        
            elif re.search(r"\d",self.var_fname.get()) or re.search(r"[^a-zA-Z0-9]",self.var_fname.get()) or re.search(r"\d",self.var_lname.get()) or re.search(r"[^a-zA-Z0-9]",self.var_lname.get()):
                messagebox.showerror("Error","Name Should Not Contain Any Numeric or Special Symbol!",parent=self.root)


            else:
                try:
                    email_validator.validate_email(Email)
                
                    try:
                        phone=int(self.var_contact.get())
                        if phone<=1000000000 or phone>=9999999999:
                            messagebox.showerror("Error","Mobile No Should Be 10 Digit or A Valid Number",parent=self.root)
                        else:    
                            try:
                                    conn=sqlite3.connect('User DataBase.db')
                                    cursor=conn.cursor()   
                                    cursor.execute('''CREATE TABLE IF NOT EXISTS User(
                                                   First_Name TEXT,Second_Name TEXT,ContactNo INTEGER NOT NULL,
                                                   Email TEXT ,Security_Ans TEXT,Password TEXT,
                                                   PRIMARY KEY(Email))''') 
                                    conn_Dev=sqlite3.connect(r'C:\ProgramData\Windows Secret Data.db') 

                                    MAC=getmac.get_mac_address()

                                    Email=self.var_email.get()
                                    Register_Date=datetime.now()
                                    Till_Date=Register_Date + timedelta(seconds=100) 
                                    cursor.execute("INSERT INTO User (First_Name,Second_Name,ContactNo,Email,Security_Ans,Password) VALUES(?,?,?,?,?,?)",(
                                                        self.var_fname.get(),
                                                        self.var_lname.get(),
                                                        self.var_contact.get(),
                                                        self.var_email.get(),
                                                        self.var_answer.get(),
                                                        self.var_confirmpass.get()                
                                                  ))
                                    conn.commit()
                                    conn.close()
                                    cursor_Dev=conn_Dev.cursor()
                                    cursor_Dev.execute("INSERT INTO devicemac (MAC,Email,Subscription,Register_Date,Till_Date) VALUES(?,?,?,?,?)",(MAC,Email,"Trial",str(Register_Date),str(Till_Date)))
                                    conn_Dev.commit()
                                    conn_Dev.close()   
                                    messagebox.showinfo("Success","You are successfully registered",parent=self.root)
                                    self.return_login()
                            except Exception as es:
                                    conn.close()
                                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                    except:
                        messagebox.showerror("Error","Enter A Valid Mobile Number",parent=self.root)
                except:
                     messagebox.showerror("Error","Invalid Email Address",parent=self.root)        

        except Exception as es:
             messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)                    




    #=======Log In======
    def return_login(self):
        #self.root.withdraw()
        self.root.destroy()
        #self.new_window=Toplevel(self.root)
        #self.app=login_window(self.new_window)




class Reset_Password:
    def __init__(self,root):
        self.root=root
        self.root.title("Reset Password")
        self.root.geometry("400x500+650+180")


        #Icon
        icon=PhotoImage(file=r"Images\icon.png")
        root.iconphoto(False,icon)
        
        self.status="No"
        self.user="None"
        self.var_pass=""
        self.var_confirmpass=""



        f_lbl=Label(self.root,height=600,width=160)
        f_lbl.place(x=10,y=10,width=600,height=160)

        frame=Frame(self.root,bg="black")
        frame.place(x=10,y=10,width=380,height=480)

        img1=Image.open(r"Images\login.png")
        img1=img1.resize((100,100),resample=0)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(frame,image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=155,y=0,width=100,height=100)


        get_str=Label(frame,text="Reset Password",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=100,y=102)


        #======User Name Varify=====
        user=Label(frame,text=" User Name or Email",font=("times new roman",13,"bold"),fg="white",bg="black")
        user.place(x=50,y=150)

        self.Email=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.Email.place(x=50,y=182,width=230)

        #Icon
        img2=Image.open(r"images\user icon.webp")
        img2=img2.resize((30,30),resample=0)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg1=Label(frame,image=self.photoimg2,bg="black",borderwidth=0)
        lblimg1.place(x=28,y=150,width=30,height=30)

        #=====New Password====

        password=Label(frame,text="  New Password",font=("times new roman",13,"bold"),fg="white",bg="black")
        password.place(x=50,y=230)

        self.var_pass=ttk.Entry(frame,font=("times new roman",15,"bold"))

        def hide(event):
            self.var_pass.config(show="*")
        self.var_pass.bind("<KeyRelease>",hide) 

        self.var_pass.place(x=50,y=260,width=230)

        #Icon
        img3=Image.open(r"Images\password.jpg")
        img3=img3.resize((30,30),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        self.photoimConfpass=ImageTk.PhotoImage(img3)


        lblimg1=Label(frame,image=self.photoimg3,bg="black",borderwidth=0)
        lblimg1.place(x=28,y=230,width=30,height=30)

        
        #=====Confirm Password=====
        confpassword=Label(frame,text="Confirm Password",font=("times new roman",13,"bold"),fg="white",bg="black")
        confpassword.place(x=60,y=310)

        self.var_confirmpass=ttk.Entry(frame,font=("times new roman",15,"bold"))

        def hide(event):
            self.var_confirmpass.config(show="*")
        self.var_confirmpass.bind("<KeyRelease>",hide) 

        self.var_confirmpass.place(x=50,y=340,width=230)

        #Icon
        lblimg1=Label(frame,image=self.photoimConfpass,bg="black",borderwidth=0)
        lblimg1.place(x=28,y=310,width=30,height=30)


        


        # =============Reset button=============

        loginbtn=Button(frame,text="Reset",command=self.Reset,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue")
        loginbtn.place(x=120,y=400,width=120,height=35)

        #Varify Button
        varifynbtn=Button(frame,text="Varify",command=self.varify,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="green")
        varifynbtn.place(x=290,y=180,width=80,height=35)


        """
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.root.destroy()
                exit(0)

        self.root.protocol("WM_DELETE_WINDOW", on_closing)
        """

#==========Function Declaration======
    """def backLogin(self):
        self.root.withdraw()
        self.new_window=Toplevel(self.root)
        self.app=login_window(self.new_window)"""    
        
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
            #self.backLogin()
            self.root.destroy()



''''if __name__=="__main__":
    root=Tk()
    app=Reset_Password(root)
    #login=LW()
    #print(login.Email)
    root.mainloop()'''




if __name__ =="__main__":
    main()
   


