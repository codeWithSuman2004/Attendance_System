from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox



class Developer:
    def __init__(self,root):
        self.root=root
        root.title("Developers")
        root.geometry('1300x620+180+80')
        root.configure(bg="cyan2")

        #Icon
        icon=PhotoImage(file=r"Images\icon.png")
        root.iconphoto(False,icon)

        img1=Image.open(r"Images\DevBG.jpeg")
        img1=img1.resize((1280,600),resample=0)
        self.photoimg1=ImageTk.PhotoImage(img1)

        BgImg=Label(self.root,image=self.photoimg1)
        BgImg.place(x=10,y=12,width=1280,height=600)

        #Home
        home=Button(BgImg,text="Back",command=self.backHome,width=17,font=("times new roman", 30, "bold"),bg="seagreen1",fg="black")
        home.place(x=995,y=2,width=242,height=50)

        #Developers Text
        Devtxt=Label(self.root,text="Our Team Members",font=("times new roman",20,"bold"),bg="white",fg="navy",anchor="w")
        Devtxt.place(x=500,y=10,bordermode=INSIDE)


        #Pradip
        Pradip=Image.open(r"Images\Pradip.jpg")
        Pradip=Pradip.resize((200,200))
        self.photoPradip=ImageTk.PhotoImage(Pradip)

        Pradip=Label(BgImg,image=self.photoPradip)
        Pradip.place(x=40,y=65)

        Pradiptxt=Label(self.root,text="  Pradip Bauri ",font=("times new roman",20,"bold"),bg="white",fg="navy",anchor="w")
        Pradiptxt.place(x=52,y=280,width=204,height=35,bordermode=INSIDE)


        #Suman
        Suman=Image.open(r"Images\Suman.jpg")
        Suman=Suman.resize((200,200))
        self.photoSuman=ImageTk.PhotoImage(Suman)

        Suman=Label(BgImg,image=self.photoSuman)
        Suman.place(x=345,y=65)
        Sumantxt=Label(self.root,text="    Suman Mal ",font=("times new roman",20,"bold"),bg="white",fg="navy",anchor="w")
        Sumantxt.place(x=357,y=280,width=204,height=35,bordermode=INSIDE)


        #Susanta
        Susanta=Image.open(r"Images\Susanta.jpg")
        Susanta=Susanta.resize((200,200))
        self.photoSusanta=ImageTk.PhotoImage(Susanta)

        Susanta=Label(BgImg,image=self.photoSusanta)
        Susanta.place(x=670,y=65)
        Susantatxt=Label(self.root,text="Susanta Malgope",font=("times new roman",20,"bold"),bg="white",fg="navy",anchor="w")
        Susantatxt.place(x=682,y=280,width=204,height=35,bordermode=INSIDE)


        #Sougata
        Sougata=Image.open(r"Images\Sougata.jpg")
        Sougata=Sougata.resize((236,200))
        self.photoSougata=ImageTk.PhotoImage(Sougata)

        Sougata=Label(BgImg,image=self.photoSougata)
        Sougata.place(x=995,y=65)
        Sougatatxt=Label(self.root,text="Sougata Das Modak",font=("times new roman",20,"bold"),bg="white",fg="navy",anchor="w")
        Sougatatxt.place(x=1007,y=280,width=240,height=35,bordermode=INSIDE)

        #Bristi
        Bristi=Image.open(r"Images\Bristi.jpg")
        Bristi=Bristi.resize((200,200))
        self.photoBristi=ImageTk.PhotoImage(Bristi)

        Bristi=Label(BgImg,image=self.photoBristi)
        Bristi.place(x=40,y=330)

        Bristitxt=Label(self.root,text="    Bristi Dey ",font=("times new roman",20,"bold"),bg="white",fg="navy",anchor="w")
        Bristitxt.place(x=52,y=550,width=204,height=35,bordermode=INSIDE)


        

        #Pintu
        Pintu=Image.open(r"Images\Pintu.png")
        Pintu=Pintu.resize((200,200))
        self.photoPintu=ImageTk.PhotoImage(Pintu)

        Pintu=Label(BgImg,image=self.photoPintu)
        Pintu.place(x=345,y=330)
        Pintutxt=Label(self.root,text="Pintu Karmakar",font=("times new roman",20,"bold"),bg="white",fg="navy",anchor="w")
        Pintutxt.place(x=357,y=550,width=204,height=35,bordermode=INSIDE)


        #Anup
        Anup=Image.open(r"Images\Anup.jpg")
        Anup=Anup.resize((200,200))
        self.photoAnup=ImageTk.PhotoImage(Anup)

        Anup=Label(BgImg,image=self.photoAnup)
        Anup.place(x=670,y=330)
        Anuptxt=Label(self.root,text="   Anup Mandal",font=("times new roman",20,"bold"),bg="white",fg="navy",anchor="w")
        Anuptxt.place(x=682,y=550,width=204,height=35,bordermode=INSIDE)


        #Biplab
        Biplab=Image.open(r"Images\Biplab.jpg")
        Biplab=Biplab.resize((236,200))
        self.photoBiplab=ImageTk.PhotoImage(Biplab)

        Biplab=Label(BgImg,image=self.photoBiplab)
        Biplab.place(x=995,y=330)
        Biplabtxt=Label(self.root,text="        Biplab Pal",font=("times new roman",20,"bold"),bg="white",fg="navy",anchor="w")
        Biplabtxt.place(x=1007,y=550,width=240,height=35,bordermode=INSIDE)


    def backHome(self):
        self.root.destroy()    


        


        



if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()






