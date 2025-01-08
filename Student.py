from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
from tkcalendar import DateEntry
from tkinter import messagebox
import string
import sqlite3
import email_validator
import cv2
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta
import re
#from main import Face_Recognition_System

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        icon=PhotoImage(file=r"Images\icon.png")
        root.iconphoto(False,icon)

        #======Varables=====
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_stream=StringVar()
        self.var_semester=StringVar()
        self.var_div=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_radio=StringVar()
        self.student_Roll=[]
        self.radio=StringVar()
        
        self.previousID=-25

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
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT",font=("times new roman",35,"bold","italic"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #----Frame-----
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55, width=1480,height=600)

        #left-label-frame
        Left_frame=LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10, width=730, height=580)


        left_img=Image.open(r"Images\bg1.jpg")
        left_img=img2.resize((500,150))
        self.photo_left_img=ImageTk.PhotoImage(left_img)

        f_lbl=Label(Left_frame,image=self.photo_left_img)
        f_lbl.place(x=5,y=0,width=720, height=130)

        #current course
        current_course_frame=LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current cource",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135, width=720,height=150)


        #Stream
        stream_label=Label(current_course_frame, text="Stream:", font=("times new roman", 13, "bold"),bg="white") 
        stream_label.grid(row=0,column=0)

        stream_combo=ttk.Combobox(current_course_frame,textvariable=self.var_stream,font=("times new roman", 12, "bold"),state="Read Only")
        stream_combo["values"]=("Select Stream","Science","Arts","Commerce")
        
        stream_combo.current(0)
        stream_combo.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        

        #Department
        dep_label=Label(current_course_frame, text="Department:", font=("times new roman", 13, "bold"),bg="white") 
        dep_label.grid(row=0,column=2)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman", 12, "bold"),state="Read Only")
        dep_combo["values"]=("Select Department","Select Stream First")
        def save_value(event):
            # Get the current value
            current_value = stream_combo.get()
            # Now you can use this value to check the next combobox value
            if current_value=="Science":
                dep_combo["values"]=("Computer Science","Chemistry","Mathematics","Physics")
            elif current_value=="Arts":
                dep_combo["values"]=("Bengali","Sanskrit","English","Polytical Science","History")
            else:
                dep_combo["values"]=("Economics","Accountancy","Statistics")

        # Bind the function to the combobox
        stream_combo.bind("<<ComboboxSelected>>", save_value)
        
        dep_combo.grid(row=0,column=3,padx=5,pady=5,sticky=W)
        dep_combo.current(0)

        #===Course Type===
        cource_Type_label=Label(current_course_frame, text="Course Type:", font=("times new roman", 13, "bold"),bg="white") 
        cource_Type_label.grid(row=1,column=0,pady=10,sticky=W)

        cource_Type_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman", 12, "bold"),state="Read Only")
        cource_Type_combo["values"]=("Select Course","Hons","Program")
        cource_Type_combo.current(0)
        cource_Type_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Semester
        sem_label=Label(current_course_frame, text="Semester:", font=("times new roman", 13, "bold"),bg="white") 
        sem_label.grid(row=1,column=2,pady=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman", 12, "bold"),state="Read Only")
        sem_combo["values"]=("Select Semester","1st Sem","2nd Sem","3st Sem","4th Sem","5th Sem","6th Sem")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,pady=10,sticky=W)

        #Class Student information
        Class_Student_frame=LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student information",font=("times new roman",12,"bold"))
        Class_Student_frame.place(x=5,y=250, width=720,height=300)

        #Student ID
        studentID_label=Label(Class_Student_frame, text="StudentID:", font=("times new roman", 13, "bold")) 
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)       

        studentID_Entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman", 13, "bold"))

        def studentID_check(event):
             if self.var_std_id.get()!="":
                try:
                     int(self.var_std_id.get())
                except:
                     messagebox.showerror("Error","ID should be integer",parent=self.root)
        studentID_Entry.bind("<KeyRelease>", studentID_check)
        
        studentID_Entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student Name
        studentName_label=Label(Class_Student_frame, text="Student Name:", font=("times new roman", 13, "bold")) 
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)       

        studentName_Entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman", 13, "bold"))

        def check_StudentName(event):
             if self.var_std_name.get()!="" and re.search(r"\d",self.var_std_name.get().replace(" ","")) or re.search(r"[^a-zA-Z0-9]",self.var_std_name.get().replace(" ","")):
                messagebox.showerror("Error","Name Should Not Contain Any Numeric or Special Symbol!",parent=self.root)

        studentName_Entry.bind("<KeyRelease>",check_StudentName)        

        studentName_Entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Class Division
        student_div_label=Label(Class_Student_frame, text="Class Division:", font=("times new roman", 13, "bold")) 
        student_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)       

        student_div_Entry=ttk.Combobox(Class_Student_frame,textvariable=self.var_div,width=20,font=("times new roman", 13, "bold"),state="Read Only")
        student_div_Entry["values"]=("Select Division","A","B","C")
        student_div_Entry.current(0)
        student_div_Entry.grid(row=1,column=3,pady=10,sticky=W)


        student_div_Entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll No
        Roll_no_label=Label(Class_Student_frame, text="Roll No:", font=("times new roman", 13, "bold")) 
        Roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)       

        Roll_no_Entry=ttk.Entry(Class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman", 13, "bold"))
        
        def studentRoll_check(event):
             if self.var_roll.get()!="":
                try:
                     int(self.var_roll.get())
                except:
                     messagebox.showerror("Error","Roll No should be integer",parent=self.root)    
        Roll_no_Entry.bind("<KeyRelease>", studentRoll_check)


        Roll_no_Entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        Gender_label=Label(Class_Student_frame, text="Gender:", font=("times new roman", 13, "bold")) 
        Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)       

        Gender_Entry=ttk.Combobox(Class_Student_frame,textvariable=self.var_gender,font=("times new roman", 12, "bold"),state="Read Only")
        Gender_Entry["values"]=("Select Gender","Male","Female","Other")
        Gender_Entry.current(0)
        Gender_Entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
        DOB_label=Label(Class_Student_frame, text="DOB(MM.DD.YY):", font=("times new roman", 13, "bold")) 
        DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)       

        DOB_Entry=DateEntry(Class_Student_frame,textvariable=self.var_dob,width=18,font=("times new roman", 13, "bold"))
        
        def check_date(event):

            selected_date = datetime.strptime(self.var_dob.get(), "%m/%d/%y")
            current_date = datetime.now()
            if selected_date.date() > current_date.date():
                 messagebox.showerror("Error","You Can't Set Upcoming Date",parent=self.root)
            elif (current_date.date() < selected_date.date()+relativedelta(years=15)):
                  messagebox.showerror("Error","Age Should be Greater than 15",parent=self.root)
        DOB_Entry.bind("<<DateEntrySelected>>", check_date)

        DOB_Entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #Email
        Email_label=Label(Class_Student_frame, text="Email:", font=("times new roman", 13, "bold")) 
        Email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)       

        Email_Entry=ttk.Entry(Class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman", 13, "bold"))
        Email_Entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone No
        Phone_label=Label(Class_Student_frame, text="Phone No:", font=("times new roman", 13, "bold")) 
        Phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)       

        Phone_Entry=ttk.Entry(Class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman", 13, "bold"))
        
        def Phone_check(event):
             if self.var_phone.get()!="":
                try:
                     int(self.var_phone.get())
                except:
                     messagebox.showerror("Error","Phone No should be integer",parent=self.root)    
        Phone_Entry.bind("<KeyRelease>", Phone_check)

        Phone_Entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        Address_label=Label(Class_Student_frame, text="Address:", font=("times new roman", 13, "bold")) 
        Address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)       

        Address_Entry=Entry(Class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman", 13, "bold"))
        Address_Entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher Name
        Teacher_label=Label(Class_Student_frame, text="Teacher Name:", font=("times new roman", 13, "bold")) 
        Teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)       

        Teacher_Entry=ttk.Entry(Class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman", 13, "bold"))
        def check_TeacherName(event):
            if self.var_teacher.get()!="" and re.search(r"\d",self.var_teacher.get().replace(" ","")) or re.search(r"[^a-zA-Z0-9]",self.var_teacher.get().replace(" ","")):
                messagebox.showerror("Error","Teacher Name Should Not Contain Any Numeric or Special Symbol!",parent=self.root)

        Teacher_Entry.bind("<KeyRelease>", check_TeacherName)       


        Teacher_Entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #Radio Buttons
        radiobutton1=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio,text="Take Photo Sample",value="Yes")
        radiobutton1.grid(row=6,column=0)

        radiobutton2=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio,text="No Photo Sample",value="No")
        radiobutton2.grid(row=6,column=1)

        #Buttons Frame

        #Back
        home=Button(bg_img,text="Back",command=self.Back,width=17,font=("times new roman", 30, "bold"),bg="Purple4",fg="white")
        home.place(x=1300,y=0,width=200,height=45)

        btn_frame=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=215,width=715,height=34)

        #save
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        #Update
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        #Delete
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        #Reset
        Reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        Reset_btn.grid(row=0,column=3)

        #2nd Button Frame
        btn_frame1=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=245,width=715,height=35)

        #Take Photo
        take_photo_btn=Button(btn_frame1,text="Take Photo",command=self.generate_dataset,width=34,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        #Update Photo
        update_photo_btn=Button(btn_frame1,text="Update Photo",width=35,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)


        #Right label frame 
        Right_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE, text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10, width=720, height=588)

        right_img=Image.open(r"Images\bg1.jpg")
        right_img=img2.resize((500,150))
        self.photo_right_img=ImageTk.PhotoImage(right_img)

        f_lbl=Label(Right_frame,image=self.photo_right_img)
        f_lbl.place(x=5,y=0,width=720, height=130)

        #=======Search System========
        Search_frame=LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=150, width=710,height=70)

        Search_label=Label(Search_frame, text="Search BY:", font=("times new roman", 13, "bold"),bg="green",fg="white") 
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)       

        Search_combo=ttk.Combobox(Search_frame,font=("times new roman", 12, "bold"),state="Read Only",width=15)
        Search_combo["values"]=("Select","Roll No","Phone No","Name")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,pady=10,padx=2,sticky=W)

        Search_Entry=ttk.Entry(Search_frame,width=15,font=("times new roman", 13, "bold"))
        Search_Entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        #Search
        Search_btn=Button(Search_frame,text="Search",width=14,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3)

        #Show All
        ShowAll_photo_btn=Button(Search_frame,text="Show All",width=14,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        ShowAll_photo_btn.grid(row=0,column=4)

        #=========Table Frame=======
        Table_frame=Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        Table_frame.place(x=5,y=210, width=710,height=350)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(Table_frame,column=("Name","ID","Roll","Stream","Dep","Course","Sem","Div","Gender","DOB","Email","Phone","Address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Stream", text="Stream")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Dep", text="Department")
        self.student_table.heading("Sem", text="Semester")
        self.student_table.heading("ID", text="StudentId")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Div", text="Division")
        self.student_table.heading("Roll", text="Roll No")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB(DD/MM/YY)")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        
        self.student_table["show"]="headings"

        self.student_table.column("Stream", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Dep", width=100)
        self.student_table.column("Sem", width=100)
        self.student_table.column("ID", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Roll", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("Div", width=100)
        self.student_table.column("DOB", width=120)
        self.student_table.column("Email", width=100)
        self.student_table.column("Phone", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)


        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


        """def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.root.destroy()
                exit(0)

        self.root.protocol("WM_DELETE_WINDOW", on_closing)"""
        

    #======Function Declaration====== 

    def Back(self):
        self.root.destroy() 


    def add_data(self):
        selected_date = datetime.strptime(self.var_dob.get(), "%m/%d/%y")
        current_date = datetime.now()

        if self.var_stream.get()=="Select Stream" or self.var_dep.get()=="Select Department" or self.var_dep.get()=="Select Stream First" or self.var_semester.get()=="Select Semester" or self.var_course.get()=="Select Course" or self.var_std_name.get()=="" or self.var_std_id.get()=="" or self.var_div.get()=="Select Division" or self.var_roll.get()=="" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()==""  or self.var_address.get()=="" or self.var_teacher.get()=="" or self.var_radio.get()=="":
            messagebox.showerror("Error","All fields are Required",parent=self.root)

        elif selected_date.date() > current_date.date():
            messagebox.showerror("Error","You Can't Set Upcoming Date",parent=self.root)

        elif current_date.date() < selected_date.date()+relativedelta(years=15):
            messagebox.showerror("Error","Age Should Be Greater than 15 Years Old",parent=self.root)

        elif re.search(r"\d",self.var_std_name.get().replace(" ","")) or re.search(r"[^a-zA-Z0-9]",self.var_std_name.get().replace(" ","")):
            messagebox.showerror("Error","Name Should Not Contain Any Numeric or Special Symbol!",parent=self.root)

        elif re.search(r"\d",self.var_teacher.get().replace(" ","")) or re.search(r"[^a-zA-Z0-9]",self.var_teacher.get().replace(" ","")):
            messagebox.showerror("Error","Teacher Name Should Not Contain Any Numeric or Special Symbol!",parent=self.root)     

        else:
            try:
                int(self.var_std_id.get()) and int(self.var_roll.get()) and int(self.var_phone.get())
                phone=int(self.var_phone.get())
                email=self.var_email.get()
                if phone<=1000000000 or phone>=9999999999:
                    messagebox.showerror("Error","Mobile No Should Be 10 Digit or A Valid Number",parent=self.root)
                else:
                     try:
                        email_validator.validate_email(email)           
    
                        try:
                            conn=sqlite3.connect('Face Recognizer.db')
                            cursor=conn.cursor()
                            cursor.execute('''CREATE TABLE IF NOT EXISTS student(
                                           Name TEXT,StudentID  INTEGER NOT NULL,RollNo INTEGER NOT NULL UNIQUE,
                                           Stream TEXT,Department TEXT,Course_Type TEXT,Sem TEXT,
                                           Div TEXT,
                                           Gender TEXT,DOB TEXT,
                                           Email TEXT,PhoneNo INTEGER,Address TEXT,Teacher_Name TEXT,
                                           Photosample TEXT,
                                           PRIMARY KEY(StudentID,RollNo))'''
                                           )
                            if int(self.var_roll.get()) in self.student_Roll:
                                 messagebox.showerror("Error",f'{self.var_roll.get()} This Roll No is already in Database',parent=self.root)   
                            else:     
                                cursor.execute("INSERT INTO student (Stream,Department,Course_Type,Sem,StudentID,Name,Div,RollNo,Gender,DOB,Email,PhoneNo,Address,Teacher_Name,Photosample) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                                
                                                                                                                self.var_stream.get(),
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio.get()
                                                                                                                                ))
                                conn.commit()
                                self.fetch_data()
                                if self.var_radio.get()!="No":
                                     messagebox.showinfo("Photo","Photo Capturing Soon...",parent=self.root)
                                     self.generate_dataset()
                                conn.close()
                                messagebox.showinfo("Info","Student Details Has Been added Successfully",parent=self.root)
                        except Exception as es:
                            conn.close()
                            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                     except:
                        messagebox.showerror("Error","Invalid Email Address",parent=self.root)
            except:
                messagebox.showerror("Error","Student ID, ROll No, Phone NO should be Integer",parent=self.root)



    #=====Fetch Data====
    def fetch_data(self):
            try:
                conn=sqlite3.connect('Face Recognizer.db')
                cursor=conn.cursor()
                cursor.execute("SELECT * FROM student ORDER BY Name")
                data=cursor.fetchall()
                cursor.execute("SELECT RollNo FROM student")
                data_roll=cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    a=0
                    for i in data_roll:
                         self.student_Roll.append(data_roll[a])
                         a=a+1  
                    self.student_Roll = [item[0] for item in data_roll]    
                    conn.commit()
                else:
                     messagebox.showinfo("Info","No Details is Available To view\nAdd Data To View",parent=self.root)
                conn.close()   

            except Exception as es:
                conn.close()
                messagebox.showerror("error",f"Due To :{str(es)}",parent=self.root)

    #======get cursor=====
    def get_cursor(self,event=""):
        try:
            cursor_focus=self.student_table.focus()
            content=self.student_table.item(cursor_focus)

            if len(content)!=0:

                data=content["values"]
                self.var_std_name.set(data[0]),
                self.var_std_id.set(data[1]),
                self.var_roll.set(data[2]),
                self.var_stream.set(data[3]),
                self.var_dep.set(data[4]),
                self.var_course.set(data[5]),
                self.var_semester.set(data[6]),
                self.var_div.set(data[7]),
                self.var_gender.set(data[8]), 
                self.var_dob.set(data[9]),
                self.var_email.set(data[10]),
                self.var_phone.set(data[11]), 
                self.var_address.set(data[12]), 
                self.var_teacher.set(data[13]), 
                self.var_radio.set(data[14])

                self.radio=data[14]

                self.previousID=data[1]
        
            else:
                messagebox.showinfo("Info","No Details is Available To view\nAdd Data To View",parent=self.root)
        except Exception as es:
             messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    #======delete====
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID must be reqired",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Question?","Do you want to Delete this student details",parent=self.root)
                if delete>0:
                    conn=sqlite3.connect('Face Recognizer.db')
                    cursor=conn.cursor()
                    sql="DELETE FROM student WHERE StudentID=?"
                    value=(self.var_std_id.get(),)
                    cursor.execute(sql,value)
                else:
                    if not delete:
                        return
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Student Details Deleted Successfully",parent=self.root)
                self.reset_data()
                self.fetch_data()
            except Exception as es:
                        conn.close()
                        messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)    




    #====Upadte Function====
    def update_data(self):

        if self.var_stream.get()=="Select Stream" or self.var_dep.get()=="Select Department" or self.var_dep.get()=="Select Stream First" or self.var_semester.get()=="Select Semester" or self.var_course.get()=="Select Course" or self.var_std_name.get()=="" or self.var_std_id.get()=="" or self.var_div.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()==""  or self.var_address.get()=="" or self.var_teacher.get()=="" or self.var_radio.get()=="":
            messagebox.showerror("Error","All fields are Required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this student details",parent=self.root)
                if Update!=True:
                    if not Update:
                         return
                else:      
                    email=self.var_email.get()
                    selected_date = datetime.strptime(self.var_dob.get(), "%m/%d/%y")
                    current_date = datetime.now()

                    if selected_date.date() > current_date.date():
                        messagebox.showerror("Error","You Can't Set Upcoming Date",parent=self.root)

                    elif current_date.date() < selected_date.date()+relativedelta(years=15):
                        messagebox.showerror("Error","Age Should Be Greater than 15 Years Old",parent=self.root)
                    
                    elif re.search(r"\d",self.var_std_name.get().replace(" ","")) or re.search(r"[^a-zA-Z0-9]",self.var_std_name.get().replace(" ","")):
                         messagebox.showerror("Error","Name Should Not Contain Any Numeric or Special Symbol!",parent=self.root)

                    elif re.search(r"\d",self.var_teacher.get().replace(" ","")) or re.search(r"[^a-zA-Z0-9]",self.var_teacher.get().replace(" ","")):
                         messagebox.showerror("Error","Teacher Name Should Not Contain Any Numeric or Special Symbol!",parent=self.root)
                    
                    elif self.previousID != int(self.var_std_id.get()):
                        messagebox.showerror("Error","You Can't Update ID",parent=self.root)

                    else:

                        try:
                            phone=int(self.var_phone.get())
                            if phone<=1000000000 or phone>=9999999999:
                                messagebox.showerror("Error","Mobile No Should Be 10 Digit or A Valid Number",parent=self.root)
                            else:
                                try:
                                    email_validator.validate_email(email)
                                    try:
                                        conn=sqlite3.connect('Face Recognizer.db')
                                        cursor=conn.cursor()      
                                        if self.radio=="Yes" and self.var_radio.get()=="No":
                                             messagebox.showwarning("Warning","Already Photo Available You Can't Deny it",parent=self.root)
                                             self.var_radio.set("Yes")
                                        cursor.execute("UPDATE student SET Stream=?,Department=?,Course_Type=?,Sem=?,Name=?,Div=?,RollNo=?,Gender=?,DOB=?,Email=?,PhoneNo=?,Address=?,Teacher_Name=?,Photosample=? WHERE StudentID=?",(
                                                                                                                self.var_stream.get(),
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio.get(),
                                                                                                                self.var_std_id.get()
                                                                                                                        ))
                                        conn.commit()
                                        self.fetch_data()
                                        if self.var_radio.get()=="Yes" and self.radio=="No":
                                            messagebox.showinfo("Info","Photo Capturing Soon...",parent=self.root)
                                            self.generate_dataset()
                                        messagebox.showinfo("Info","Student Details Updated Successfully",parent=self.root)     
                                        conn.close()
                                    except Exception as es:
                                        conn.close()
                                        messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)       

                                except:
                                    messagebox.showerror("Error","Invalid Email Address",parent=self.root)

                        
                        except:
                            messagebox.showerror("Error"," A InValid Number",parent=self.root)
                                             
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                    

    #====Reset Function===
    def reset_data(self):
        self.var_stream.set("Select Stream"),
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_semester.set("Select Semester"),
        self.var_std_name.set(""),
        self.var_div.set(""),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio.set(""),
        self.var_std_id.set("")


# =============Generate data set or Take photo samples ===========
    def generate_dataset(self):
        if self.var_stream.get()=="Select Stream" or self.var_dep.get()=="Select Department" or self.var_dep.get()=="Select Stream First" or self.var_semester.get()=="Select Semester" or self.var_course.get()=="Select Course" or self.var_std_name.get()=="" or self.var_std_id.get()=="" or self.var_div.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()==""  or self.var_address.get()=="" or self.var_teacher.get()=="" or self.var_radio.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        elif self.var_radio.get()=="No":
                 messagebox.showerror("Error","You Have Selected No Photo",parent=self.root)
        else:
                try:
                    conn=sqlite3.connect('Face Recognizer.db')
                    cursor=conn.cursor()
                    cursor.execute("select * from student")
                    myresult=cursor.fetchall()
                    id=0
                    for x in myresult:
                        id+=1                                                                                                                                                                                                                                                                                                                                                                                            
                    cursor.execute("UPDATE student SET Photosample=? WHERE StudentID=?",(
                        
                                                                                                    self.var_radio.get(),
                                                                                                    self.var_std_id.get()
                                                                                                            ))
                    conn.commit()
                    self.fetch_data()
                    
                    conn.close()
    
        
    #========== Load predefined data on face frontals from opencv=========
    
                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                    
                    def face_cropped(img):
                    
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.5,5)
                        #scaling factor=1.3
                        #Minimum Neighbor=5
    
                        for(x,y,w,h) in faces:
                            face_cropped=img[y:y+h+1,x:x+w+1]
                            return face_cropped
                    cap=cv2.VideoCapture(1)
                    img_id=0
                    while (True):
                        ret,my_farme=cap.read()
                        my_farme=cv2.flip(my_farme,1)
                        cv2.imshow("Camera Is Ready To Capture Press C",my_farme)
                        if cv2.waitKey(1)==ord('c'):
                             break
                    cap=cv2.VideoCapture(1)      
                    while True:
                        ret,my_farme=cap.read()
                        my_farme=cv2.flip(my_farme,1)
                        if face_cropped(my_farme) is not None:
                            img_id+=1
                        face=cv2.resize(face_cropped(my_farme),(600,600))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        face=cv2.medianBlur(face,5)
                        #file_name_path="Data/"+self.var_std_name.get() +"..."+self.var_roll.get()+"..."+str(img_id)+".jpg"
                        file_name_path="Data/user."+self.var_std_id.get()+"."+str(img_id)+".jpg"
                        #file_name_path="Data/"+self.var_std_name.get()+"."+self.var_std_id.get()+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating data sets completed!!!!",parent=self.root)
                    #self.reset_data()
                except Exception as es:
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)





if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()