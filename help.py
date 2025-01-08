from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
from PIL import Image,ImageTk



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("810x550+500+100")
        #root.configure(bg="teal")
        self.root.title("Help Desk")


        #Icon
        icon=PhotoImage(file=r"Images\icon.png")
        root.iconphoto(False,icon)

        f_lbl=Label(self.root,height=650,width=180)
        f_lbl.place(x=8,y=8,width=660,height=180)

        frame=Frame(self.root,bg="teal")
        frame.place(x=10,y=10,width=790,height=530)


        RightFrame=Frame(frame,bg="tomato2")
        RightFrame.place(x=380,y=0,width=420,height=630)




        btnFrame=Frame(RightFrame,bg="black")
        btnFrame.place(x=270,y=0,width=140,height=40)

        #Home
        home=Button(btnFrame,text="Back",command=self.backHome,width=17,font=("times new roman", 22, "bold"),bg="seagreen1",fg="black")
        home.place(x=5,y=5,width=130,height=30)

        #===Add Text====

        Abouttxt=Label(RightFrame,text="About Us:",font=("times new roman",20,"bold"),bg="tomato2",fg="blue",anchor="w")
        Abouttxt.place(x=0,y=10,bordermode=INSIDE)

        Infotxt1=Label(RightFrame,text="Hi,",font=("times new roman",15,"bold"),bg="tomato2",anchor="w")
        Infotxt1.place(x=0,y=50,bordermode=INSIDE)

        Infotxt2=Label(RightFrame,text="We are happy to help you.We are from Bankura",font=("times new roman",15,"bold"),bg="tomato2",anchor="w")
        Infotxt2.place(x=0,y=75,bordermode=INSIDE)

        Infotxt3=Label(RightFrame,text="Sammlilani College,and we Developed this ",font=("times new roman",15,"bold"),bg="tomato2",anchor="w")
        Infotxt3.place(x=0,y=100,bordermode=INSIDE)

        Infotxt4=Label(RightFrame,text="System. If you are facing any problem, you can ",font=("times new roman",15,"bold"),bg="tomato2",anchor="w")
        Infotxt4.place(x=0,y=128,bordermode=INSIDE)

        Infotxt5=Label(RightFrame,text="reach out us using following options.",font=("times new roman",15,"bold"),bg="tomato2",anchor="w")
        Infotxt5.place(x=0,y=155,bordermode=INSIDE)


        #===Address=====
        Address=Label(RightFrame,text="Address:",font=("times new roman",25,"bold"),bg="tomato2",fg="blue",anchor="w")
        Address.place(x=0,y=240,bordermode=INSIDE)

        Addressfield1=Label(RightFrame,text="Rabindra Chhatrabas, Shikarapara,",font=("times new roman",15,"bold"),bg="tomato2",anchor="w")
        Addressfield1.place(x=0,y=280,bordermode=INSIDE)

        Addressfield2=Label(RightFrame,text="Kenduadihi, Bharat Sevashram Road,",font=("times new roman",15,"bold"),bg="tomato2",anchor="w")
        Addressfield2.place(x=0,y=310,bordermode=INSIDE)

        Addressfield3=Label(RightFrame,text="Bankura, 722102",font=("times new roman",15,"bold"),bg="tomato2",anchor="w")
        Addressfield3.place(x=0,y=335,bordermode=INSIDE)

        #===Email====
        Emailheading=Label(RightFrame,text="Email:",font=("times new roman",25,"bold"),bg="tomato2",fg="blue",anchor="w")
        Emailheading.place(x=0,y=370,bordermode=INSIDE)

        Email=Label(RightFrame,text="ColoredStack2503+FaceRecog@gmail.com",font=("times new roman",15,"bold"),bg="tomato2",fg="navy",anchor="w")
        Email.place(x=0,y=412,bordermode=INSIDE)

        #===Phone====
        Phoneheading=Label(RightFrame,text="Phone No:",font=("times new roman",25,"bold"),bg="tomato2",fg="blue",anchor="w")
        Phoneheading.place(x=0,y=440,bordermode=INSIDE)

        Email=Label(RightFrame,text="+91 1234567890",font=("times new roman",15,"bold"),bg="tomato2",fg="navy",anchor="w")
        Email.place(x=0,y=480,bordermode=INSIDE)


    
    def backHome(self):
        self.root.destroy()


        



if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
