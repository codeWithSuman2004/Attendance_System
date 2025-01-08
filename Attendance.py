from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        root.title("Attendance DataSheet")
        root.geometry('1200x500+200+200')
        root.configure(bg="black")

        #Icon
        icon=PhotoImage(file=r"Images\icon.png")
        root.iconphoto(False,icon)

        

       
        main_frame=Frame(self.root,bd=2,bg="white")
        main_frame.place(x=7,y=7,width=1180,height=480)


        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="seagreen",relief=RIDGE,text=" Attendance Details",font=("times new roman",35,))
        Right_frame.place(x=5,y=5,width=1158,height=460)

        table_frame=Frame (Right_frame, bd=2, relief=RIDGE, bg="yellow")
        table_frame.place (x=5,y=5, width=1145,height=390)

        #Open File
        openFile_btn=Button(main_frame, text="Open File",command=self.importCsv, width=17, font=("times new roman", 20, "bold"),bg="cyan",fg="black") 
        openFile_btn.place(x=700,y=13,width=200,height=45)

        #Back
        home=Button(main_frame,text="Back",command=self.backHome,width=17,font=("times new roman", 20, "bold"),bg="cyan",fg="black")
        home.place(x=950,y=13,width=200,height=45)

        # ==========scroll bar table===============
        scroll_x=ttk.Scrollbar (table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar (table_frame, orient=VERTICAL)

        self.AttendaceReportTable=ttk.Treeview(table_frame,columns=("id", "roll", "name","department", "time", "date", "attendance"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.AttendaceReportTable.xview)
        scroll_y.config(command=self.AttendaceReportTable.yview)

        self.AttendaceReportTable.heading("id", text="Attendance ID")
        self.AttendaceReportTable.heading("roll", text="Roll")
        self.AttendaceReportTable.heading("name", text="Name")
        self.AttendaceReportTable.heading("department", text="Department")
        self.AttendaceReportTable.heading("time", text="Time")
        self.AttendaceReportTable.heading("date", text="Date")
        self.AttendaceReportTable.heading("attendance", text="Attendance")
        
        self.AttendaceReportTable["show"]="headings"

        self.AttendaceReportTable.column("id", width=100)
        self.AttendaceReportTable.column("roll", width=100)
        self.AttendaceReportTable.column("name", width=100)
        self.AttendaceReportTable.column("department", width=100)
        self.AttendaceReportTable.column("time", width=100)
        self.AttendaceReportTable.column("date", width=100)
        self.AttendaceReportTable.column("attendance", width=100)

        self.AttendaceReportTable.pack(fill=BOTH, expand=1)
        #self.AttendaceReportTable.bind("<ButtonRelease>",self.get_cursor)
    


    #======Fetch Data=====
    def backHome(self):
        self.root.destroy()  


    def fetchData(self,rows):
        self.AttendaceReportTable.delete(*self.AttendaceReportTable.get_children())
        for i in rows:
            self.AttendaceReportTable.insert("",END,values=i)
     

    #====ImportCSV=====
    def importCsv(self):
        try:
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
            with open(fln) as myfile :
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)
        except Exception as es:
            messagebox.showerror("Error",f"Deu To:{str(es)}",parent=self.root)        

    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*csv"),("All File","* *")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.write(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to"+os.path.basename(fln)+"succesfully")
        except Exception as es:
            messagebox.showerror("Error",f"Deu To:{str(es)}",parent=self.root)
        


        
if __name__=="__main__":
    root=Tk()
    obj= Attendance(root)
    root.mainloop()
    
