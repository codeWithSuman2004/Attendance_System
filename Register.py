from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import re


def main():
    win=Tk()
    app=register(win)
    win.mainloop()


class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

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
        fname_entry.place(x=50,y=130,width=250)

        # last name------------

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="black",fg="yellow")
        lname.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        # contact-----------------

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="black",fg="yellow")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
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
        self.password.place(x=50,y=340,width=250)

        # confirm password--------------------

        confirm=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="black",fg="yellow")
        confirm.place(x=370,y=310)

        self.confirm=ttk.Entry(frame,textvariable=self.var_confirmpass,font=("times new roman",15))
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

        # function declaration----------------------------------
    def register(self):
        phone = int(self.var_contact.get())
        if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_email.get()=="" or self.var_contact.get()=="" or self.var_question.get()=="Select" or self.var_answer.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confirmpass.get():
            messagebox.showerror("Error","Password and Confirm Password must be same",parent=self.root)
        
        elif re.search(r"\d",self.var_fname.get()) or re.search(r"[^a-zA-Z0-9]",self.var_fname.get()) or re.search(r"\d",self.var_lname.get()) or re.search(r"[^a-zA-Z0-9]",self.var_lname.get()):
            messagebox.showerror("Error","Name Should Not Contain Any Numeric or Special Symbol!",parent=self.root)
                  
        #phone = int(self.var_contact.get())   

        elif phone<=1000000000 or phone>=9999999999:
            messagebox.showerror("Error","Mobile No Should Be 10 Digit or A Valid Number",parent=self.root)     

        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our Terms and Conditions",parent=self.root)
        else:
            messagebox.showinfo("Success","You are successfully registered,Now click the login button to proceed",parent=self.root)       



    def return_login(self):
        self.root.destroy()


if __name__ =="__main__":
    main()