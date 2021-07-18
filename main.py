from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
class Qr_generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry(900*500 +200+50)
        self.root.title("QR Generator |Developed by Anuradha")
        self.root.resizable(False,False)

        title=Label(self.root ,text="Qr Code Generator",font=("times new roman",40),bg='#053246').place(x=0,y=0,relwidth=1)
        
        #====Student details window ====


        #==Variables
        self.var_std_code=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_designation=StringVar()


        std_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        std_Frame.place(x=50,y=100,width=500,height=380)

        std_title=Label(std_Frame,text="Student details",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)
         
        lbl_std_code=Label(std_Frame,text="Student ID",font=("times new roman",15,'bold'),bg='white').place(x=20,y=60)
        lbl_name=Label(std_Frame,text="Name",font=("times new roman",15,'bold'),bg='white').place(x=20,y=100)
        lbl_department=Label(std_Frame,text="Deparment",font=("times new roman",15,'bold'),bg='white').place(x=20,y=140)
        lbl_designation=Label(std_Frame,text="Designation",font=("times new roman",15,'bold'),bg='white').place(x=20,y=180)

        txt_std_code=Entry(std_Frame,font=("times new roman",15),textvariable=self.var_stud_code,bg='lightyellow').place(x=200,y=60)
        txt_name=Entry(std_Frame,font=("times new roman",15),textvariable=self.var_name,bg='lightyellow').place(x=200,y=100)
        txt_department=Entry(std_Frame,font=("times new roman",15),textvariable=self.var_department,bg='lightyellow').place(x=200,y=140)
        txt_designation=Entry(std_Frame,font=("times new roman",15),textvariable=self.var_designation,bg='lightyellow').place(x=200,y=180)

        btn_generate = Button(std_Frame,Text='QR Genarate',command=self.generate,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=90,y=250,width=180,height=30)
        btn_clear = Button(std_Frame,text='Clear',command=self.clear,font = ("times new roman",18,'bold'),bg='#607d8b',fg='white').place(x=280,y=250,width=120,height=30)

        self.msg=''
        self.lbl_msg=Label(std_Frame,text=self.msg,font=("times new roman",20,'bold'),bg='white',fg='green')
        self.lbl_msg.place(x=0,y=310,relwidth=1)
    
    #===student qr window===

        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=600,y=100,width=250,height=380)

        std_title=Label(qr_Frame,text="Student QR Code",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)
         
        self.qr_code=Label(qr_Frame,text="No Qr\nAvailable",font=("times new roman",15),bg='#3f51b5',fg='white').place(x=0,y=0,relwidth=1)
        self.qr_code.place(x=35,y=100,width=180,height=180)

    def clear(self):
        self.var_std_code.set('')
        self.var_name.set('')
        self.var_deparment.set('')
        self.var_designation.set('')

        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')   

    def generate(self):
        if self.var_designation.get()==''or self.var_std_code.get()==''or self.var_department.get()==''or self.var_name.get()=='':
            self.msg='All Fields are required!!'
            self.lbl_msg.config(text=self.msg,fg='red')   
        else:
            qr_data=(f"Student ID: {self.var_stud_code.get()}\nStudent Name: {self.var_name.get()}\nDepartment: {self.var_deparment.get()}\nDesignation:{self.var_designation.get()}")
            qr_code=qrcode.make(qr_data)
            #print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("Student ID/Std" + str(self.var_std_code.get())+'.png')
            #image update
            self.im=ImageTk.PhotoImage(file="Student ID/Std" + str(self.var_std_code.get())+'.png')
            self.qr_code.config(image=self.im)
            #notification
            self.msg='QR Generated Successfully!!!'
            self.lbl_msg.config(text=self.msg,fg='green')   
            
    
    
    root=Tk()
    obj= Qr_generator(root)
    root.mainloop()