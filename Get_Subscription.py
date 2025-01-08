from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import getmac
from time import strftime
import time
from datetime import datetime,timedelta
from twilio.rest import Client
import random

class Payment():
    def __init__(self,root):
        self.root=root
        self.root.title("Get Subscription")
        self.root.geometry("905x650+500+100")


        #Icon
        icon=PhotoImage(file=r"Images\icon.png")
        root.iconphoto(False,icon)

        #=======Variables=====
        self.status="No"
        self.user="None"
        self.OTP=""
        self.ConfOTP=""
        self.OTPstatus="No"

        f_lbl=Label(self.root,height=650,width=180)
        f_lbl.place(x=10,y=10,width=650,height=180)

        frame=Frame(self.root,bg="SeaGreen")
        frame.place(x=10,y=10,width=885,height=630)

        frameBlack=Frame(self.root,bg="black")
        frameBlack.place(x=10,y=10,width=430,height=630)


        img1=Image.open(r"Images\Subscription.png")
        img1=img1.resize((100,100),resample=0)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(frameBlack,image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=155,y=5,width=100,height=100)


        get_str=Label(frameBlack,text="Get Subscription",font=("times new roman",20,"bold"),fg="Cyan",bg="black")
        get_str.place(x=100,y=102)


        #======User Name Varify=====
        user=Label(frameBlack,text=" User Name or Email",font=("times new roman",13,"bold"),fg="white",bg="black")
        user.place(x=60,y=170)

        self.Email=ttk.Entry(frameBlack,font=("times new roman",15,"bold"))
        self.Email.place(x=55,y=217,width=280)

        #Icon
        img2=Image.open(r"images\user icon.webp")
        img2=img2.resize((30,30),resample=0)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg1=Label(frameBlack,image=self.photoimg2,bg="black",borderwidth=0)
        lblimg1.place(x=38,y=170,width=30,height=30)

        #===== Password====

        password=Label(frameBlack,text=" Password",font=("times new roman",13,"bold"),fg="white",bg="black")
        password.place(x=60,y=265)

        self.var_pass=ttk.Entry(frameBlack,font=("times new roman",15,"bold"))

        def hide(event):
            self.var_pass.config(show="*")
        self.var_pass.bind("<KeyRelease>",hide) 

        self.var_pass.place(x=55,y=312,width=280)

        #Icon
        img3=Image.open(r"Images\password.jpg")
        img3=img3.resize((30,30),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        self.photoimConfpass=ImageTk.PhotoImage(img3)


        lblimg1=Label(frameBlack,image=self.photoimg3,bg="black",borderwidth=0)
        lblimg1.place(x=38,y=264,width=30,height=30)


        
        #=====OTP=====
        OTP=Label(frameBlack,text=" Confirm OTP",font=("times new roman",13,"bold"),fg="white",bg="black")
        OTP.place(x=70,y=450)

        self.var_OTP=ttk.Entry(frameBlack,font=("times new roman",15,"bold"))
        self.var_OTP.place(x=57,y=495,width=280)

        #Icon
        img4=Image.open(r"Images\login.png")
        img4=img4.resize((30,30),Image.LANCZOS)
        self.photoimOTP=ImageTk.PhotoImage(img4)
        lblimg1=Label(frameBlack,image=self.photoimOTP,bg="black",borderwidth=0)
        lblimg1.place(x=38,y=444,width=30,height=30)


        #======QR Code====

        #QRCode=Image.open(r"Images\QR Code.png")
        QRCode=Image.open(r"Images\QR.jpg")
        QRCode=QRCode.resize((480,480),Image.LANCZOS)
        self.QRCode=ImageTk.PhotoImage(QRCode)
        lblimg1=Label(frame,image=self.QRCode,bg="black",borderwidth=0)
        lblimg1.place(x=415,y=170)


        #=====Disclaimer Text=====

        Disclaimer=Label(frame,text="Notice:",font=("times new roman",20,"bold"),fg="White",bg="seaGreen")
        Disclaimer.place(x=430,y=5)

        Disclaimertxt=Label(frame,text="\nTo Get Subcription of 30 Days, Pay 500 Rupees on \nthis QR code And fill the OTP provided by the woner.",font=("times new roman",15,"bold"),fg="White",bg="seaGreen")
        Disclaimertxt.place(x=430,y=35,bordermode=INSIDE)


        # =============Send OTP button=============
        SendOTP=Button(frameBlack,text="Send OTP",command=self.sendOTP,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue")
        SendOTP.place(x=57,y=550,width=100,height=35)

        ConfirmOTP=Button(frameBlack,text="Confirm OTP",command=self.varifyOTP,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue")
        ConfirmOTP.place(x=190,y=550,width=150,height=35)

        #Varify User
        varifynbtn=Button(frameBlack,text="Varify User",command=self.varify,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="green")
        varifynbtn.place(x=55,y=375,width=280,height=35)


        def on_closing():
            if messagebox.askyesno("Quit", "You want to leave Subscription Page?",parent=self.root):   
                self.root.destroy()

        self.root.protocol("WM_DELETE_WINDOW", on_closing)  



#========Function Declaration=====
    def varify(self):
        if self.Email.get()=="" or self.var_pass.get()=="":
            messagebox.showerror("Error","User Name and Password required",parent=self.root)
        else:
            try:
                conn=sqlite3.connect('User DataBase.db')
                cursor=conn.cursor()
                cursor.execute("SELECT Password FROM User WHERE Email=?",(self.Email.get(),))
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
                

                if self.var_pass.get()== Password[0]:
                    self.status="Yes"
                    self.user=self.Email.get()
                    messagebox.showinfo("Success","User Varified Successfully",parent=self.root)
                else:
                    messagebox.showerror("Invalid","Invalid username or password",parent=self.root)
            except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



    #=======Send OTP====
        
    def sendOTP(self):
        if self.status=="No":
            messagebox.showwarning("warning","First Verify the User",parent=self.root)
        else:
        #elif (os.system("ping -c 1 8.8.8.8 >/dev/null 2>&1")):
            try:
            
                account_sid = 'ACf0c89dd277f45fd7fe456fcdb47135a5'
                auth_token = 'f13ef59fcc2b0b61cf19a45f3d286cba'
                self.OTP=random.randint(100000,999999)
                msg=f"OTP for Buying Subscription of Automatic Attendance System.\nOTP is {self.OTP}"
                client = Client(account_sid, auth_token)
                message = client.messages.create(
                    body=msg,
                    from_='+15078703448',  # Replace with your Twilio number
                    to='+919564280663'  # Replace with your phone number
                            )
                messagebox.showinfo("Success","OTP Sent Successfully",parent=self.root)
                self.OTPstatus="Yes"
            except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)   



    def varifyOTP(self):
         if self.OTPstatus=="No":
              messagebox.showwarning("warning","First send the OTP",parent=self.root)
         elif self.var_OTP.get()=="":
              messagebox.showwarning("warning","Fill the OTP",parent=self.root)
         elif int(self.OTP)!=int(self.var_OTP.get()):
                print(self.var_OTP.get())
                print(self.OTP)
                messagebox.showwarning("warning","OTP Does not match",parent=self.root)
         else:       
                try:

                    MAC=getmac.get_mac_address()
                    conn=sqlite3.connect(r'C:\ProgramData\Windows Secret Data.db')
                    cursor=conn.cursor()
                    cursor.execute("SELECT Till_Date FROM devicemac WHERE MAC=?",(MAC,))
                    data_TillDate=cursor.fetchall()
                    TillDate=[]
                    a=0
                    for i in data_TillDate:
                         TillDate.append(data_TillDate[a])
                         a=a+1

                    TillDate = [item[0] for item in TillDate] 
                    Till_Date=datetime.strptime(TillDate[0], '%Y-%m-%d %H:%M:%S.%f')
                    Current_Date=datetime.now()
                    if Till_Date>Current_Date:
                         Till_Date=TillDate[0] +timedelta(minutes=1.5)
                    else:     
                        Till_Date=Current_Date +timedelta(years=.000001)
                    cursor.execute("UPDATE devicemac SET Subscription=?,Till_Date=? WHERE MAC=?",("Subscription",str(Till_Date),MAC))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Subscription Buy Successfully",parent=self.root)
                    self.root.destroy()

                except Exception as es:    
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                 
                






if __name__=="__main__":
    root=Tk()
    app=Payment(root)
    root.mainloop()        