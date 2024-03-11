from tkinter import*
from tkinter import ttk
import MySQLdb
from PIL import Image,ImageTk
from tkinter import messagebox
import re
import mysql.connector 

class Register():
    def __init__(self,root):
        self.root = root
        self.root.title("Ruas Student Management")
        self.root.geometry("1600x790+0+0")

        # creation of text variable for the input entry
        self.name = StringVar()
        self.emailid = StringVar()
        self.phonenum = StringVar()
        self.gend = StringVar()
        self.studentid = StringVar()
        self.bran = StringVar()
        self.feees = StringVar()
        self.examresuult = StringVar()
        self.checkvar = IntVar()

        #Adding a backgroung image
        self.bg = ImageTk.PhotoImage(file='bg8.jpg')
        bg_lbl = Label(self.root,image =self.bg,bd=2,relief=RAISED)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #Logo image
        logo_img =Image.open('logo.png')
        #resizing the photo
        logo_img = logo_img.resize((60,60),Image.LANCZOS)
        #setting the photo
        self.photo_logo=ImageTk.PhotoImage(logo_img)


        #Ttile frame
        title_frame =Frame(self.root,bd=1,relief=RIDGE)
        title_frame.place(x=450,y=28,width=550,height=82)

        title_lbl = Label(title_frame,image=self.photo_logo,compound =LEFT,text = 'RUAS STUDENT DETAILS',font=('times new roman',28,'bold'),fg='darkblue')
        title_lbl.place(x=10,y=10)


        #informationframe
        main_frame =Frame(self.root,bd=1,relief=RIDGE)
        main_frame.place(x=450,y=110,width=550,height=560)

        #Student name
        user_name = Label(main_frame,text ='Student Name :',font=('times new roman',16,'bold'))
        user_name.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        #Student name entry
        user_entry =ttk.Entry(main_frame,textvariable=self.name,font=('times new roman',15,'bold'),width =25)
        user_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        #bind/callback  and validation with register
        validate_name = self.root.register(self.checkname)
        user_entry.config(validate='key',validatecommand=(validate_name,'%P'))


        #Email id
        Email_name = Label(main_frame,text ='Email id :',font=('times new roman',16,'bold'))
        Email_name.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        #Student name entry
        Email_entry =ttk.Entry(main_frame,textvariable=self.emailid,font=('times new roman',15,'bold'),width =25)
        Email_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        #call back and validating
        validate_email = self.root.register(self.checkemail)
        Email_entry.config(validate='key',validatecommand=(validate_email,'%P'))

        #contact
        contact = Label(main_frame,text ='Phone No :',font=('times new roman',16,'bold'))
        contact.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        #contact entry
        contact_entry =ttk.Entry(main_frame,textvariable=self.phonenum ,font=('times new roman',15,'bold'),width =25)
        contact_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)
        #call back and validating
        validate_phone = self.root.register(self.phonenumber)
        contact_entry.config(validate='key',validatecommand=(validate_phone,'%P'))


        #Student Gender (Radio buttons)
        Gender= Label(main_frame,text ='Gender:',font=('times new roman',16,'bold'))
        Gender.grid(row=3,column=0,padx=10,pady=10,sticky=W)
        #student gender entry
        # Gender_entry =ttk.Entry(main_frame,font=('times new roman',15,'bold'),width =25)
        # Gender_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        Gender_entry = Frame(main_frame) #creation of the gender entry frame
        Gender_entry.place(x=176,y=160,width=280,height=40)

        radio_male=Radiobutton(Gender_entry,variable=self.gend,value='Male',text='Male',font=('times new roman',15,'bold'))
        radio_male.grid(row=0,column=0,padx=10,pady=0,sticky=W)

        radio_female=Radiobutton(Gender_entry,variable=self.gend,value='Female',text='Female',font=('times new roman',15,'bold'))
        radio_female.grid(row=0,column=1,padx=10,pady=0,sticky=W)
        self.gend.set("Male")



        #Student id number
        StudentID = Label(main_frame,text ='Student ID No:',font=('times new roman',16,'bold'))
        StudentID.grid(row=4,column=0,padx=10,pady=10,sticky=W)
        #student id number entry
        StudentID_entry =ttk.Entry(main_frame,textvariable =self.studentid, font=('times new roman',15,'bold'),width =25)
        StudentID_entry.grid(row=4,column=1,padx=10,pady=10,sticky=W)
        #checkin and validation for student id
        validate_studentid = self.root.register(self.student_id)
        StudentID_entry.config(validate='key',validatecommand=(validate_studentid,'%P'))

        #Select branch
        branch = Label(main_frame,text ='Select Branch:',font=('times new roman',16,'bold'))
        branch.grid(row=5,column=0,padx=10,pady=10,sticky=W)
        #select branch entry
        # branch_entry =ttk.Entry(main_frame,font=('times new roman',15,'bold'),width =25)
        # branch_entry.grid(row=5,column=1,padx=10,pady=10,sticky=W)

        list1 = ['ASE','AIML','Computer science','ISE','MC','Civil','Mechanical']
        droplist =OptionMenu(main_frame,self.bran,*list1)
        droplist.config(width=21,font=('times new roman',15),bg ='white')
        self.bran.set('Select your branch')
        # droplist.place(x=240,y=420)
        droplist.grid(row=5,column=1,padx=10,pady=10,sticky=W)


        #Fee
        fee = Label(main_frame,text ='fees:',font=('times new roman',16,'bold'))
        fee.grid(row=6,column=0,padx=10,pady=10,sticky=W)
        #Fee entry
        fee_entry =ttk.Entry(main_frame,textvariable=self.feees,font=('times new roman',15,'bold'),width =25)
        fee_entry.grid(row=6,column=1,padx=10,pady=10,sticky=W)
        #checkin and validation for fee
        validate_fee = self.root.register(self.feenumber)
        fee_entry.config(validate='key',validatecommand=(validate_fee,'%P'))

        #Exam results
        exam = Label(main_frame,text ='Exam Results:',font=('times new roman',16,'bold'))
        exam.grid(row=7,column=0,padx=10,pady=10,sticky=W)
        #Exam results entry
        exam_entry =ttk.Entry(main_frame,textvariable=self.examresuult,font=('times new roman',15,'bold'),width =25)
        exam_entry.grid(row=7,column=1,padx=10,pady=10,sticky=W)
        #checin and validation of exam results
        validate_results = self.root.register(self.exam_result)
        exam_entry.config(validate='key',validatecommand=(validate_results,'%P'))

        #creating a frame for the check box
        # check_frame = Frame(main_frame,bd=2,relief=RIDGE) #creation of the gender entry frame
        # check_frame.place(x=100,y=460,width=400,height=70)

        #Saving button frame
        btn_frame = Frame(main_frame)#creation of the gender entry frame
        btn_frame.place(x=30,y=445,width=480,height=70)

        save_data =Button(btn_frame,text='Save',command=self.validation,font=('times new roman',16,'bold'),width=12,cursor='hand2',bg='blue',fg='white')
        save_data.grid(row=0,column=0,padx=1,sticky=W)

        verify_data =Button(btn_frame,text='Verify',font=('times new roman',16,'bold'),width=12,cursor='hand2',bg='blue',fg='white')
        verify_data.grid(row=0,column=1,padx=1,sticky=W)

        clear_data =Button(btn_frame,text='Clear',font=('times new roman',16,'bold'),width=12,cursor='hand2',bg='blue',fg='white')
        clear_data.grid(row=0,column=2,padx=1,sticky=W)


        # ==========================validation by mssg on evry box==================
    
    #call back function (binnding )
    def checkname(self,name):
        if name.isalnum(): # a to z and from 0 to 9
            return True
        if name == '':
            return True
        else:
            messagebox.showerror('Invalid','Not Allowed '+name[-1])


    #check for phone number
    def phonenumber(self,phone):
        if phone.isdigit():
            return True
        if len(str(phone))==0:
            return True
        else:
            messagebox.showerror('Invalid',"Invalid Entry")
            return False
        
    #check for the student id 
    def student_id(self,studentid):
        if studentid.isalnum( ): # a to z and from 0 to 9
            return True
        if studentid == '':
            return True
        else:
            messagebox.showerror('Invalid','Not Allowed '+studentid[-1])

    # check for the fees
    def feenumber(self,fee):
        if fee.isdigit():
            return True
        if len(str(fee))==0:
            return True
        else:
            messagebox.showerror('Invalid',"Invalid Entry")
            return False
        
    # check for the exam results
    def exam_result(self,result):
        if result.isfloat():
            return True
        if len(str(result))==0:
            return True
        else:
            messagebox.showerror('Invalid',"Invalid Entry")
            return False
        
    #check for the email id 
    def checkemail(self,email):
        if len(email)>3:
            if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",email):
                return True
            else:
                messagebox.showwarning('Alert','invalid email enter valid user email (example : faisalali11@gmail.com)')
                return False
        else:
            messagebox.showinfo('Invalid','Email length is too  small')
    
    #============== main validation data entry part ==============
    def validation(self):
        if self.name.get()=='':
            messagebox.showerror('Error','Please enter the name ', parent = self.root)

        elif self.emailid.get()=='':
            messagebox.showerror('Error','Please enter your email ', parent = self.root)

        elif self.phonenum.get()=='' or len(self.phonenum.get())!=10:
            messagebox.showerror('Error','Please enter your valid Phone number', parent = self.root)

        elif self.gend.get()=='':
            messagebox.showerror('Error','Please select the gender ', parent = self.root)

        elif self.studentid.get()=='':
            messagebox.showerror('Error','Please enter the stude nt id ', parent = self.root)

        elif self.bran.get()=='' or self.bran.get()== 'Select your branch':
            messagebox.showerror('Error','please select your branch ', parent = self.root)

        elif self.feees.get()=='':
            messagebox.showerror('Error','Please enter the fees ', parent = self.root)

        elif self.examresuult.get()=='':
            messagebox.showerror('Error','Please enter the result ', parent = self.root)


        elif self.emailid.get()!=None:
            x = self.checkemail(self.emailid.get())
            
        
        #=====================connecting to my sql =================
        conn = mysql.connector.connect(host ='localhost',username = 'faisalali',password = '742233', database ='ruasdetails' )
        my_cursur = conn.cursor()
        my_cursur.execute('insert into student_details values(%s,%s,%s,%s.%s,%s,%s,%s)',(
                                                                                    self.name.get(),
                                                                                    self.emailid.get(),
                                                                                    self.phonenum.get(),
                                                                                    self.gend.get(),
                                                                                    self.studentid.get(),
                                                                                    self.bran.get(),
                                                                                    self.feees.get(),
                                                                                    self.examresuult.get()
                                                                                 ))
        conn.commit()
        conn.close()

   


       
            






        

   #======================= connecting to my sql database================
            



            



if __name__ == "__main__":
    root =Tk()
    obj = Register(root)
    root.mainloop()