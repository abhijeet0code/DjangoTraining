from customtkinter import *
from tkinter import messagebox #Imported to display some warnings
from CTkToolTip import CTkToolTip #Imported for the hover message
import pymysql
from PIL import Image, ImageTk

#------------- Data Base for the SQL -------------------
def db_config():
    global mycursor
    global connection
    connection = pymysql.connect(user="root", host="127.0.0.1", database="hotel_db")
    mycursor = connection.cursor()
#--------------------------------------------------------


#------------------- Custom Tkinter ----------------------
taz=CTk()
taz.title("Hotel Management System")
#--------------------------------------------------------

#------------------------ Data Base Variable--------------------------------
usernameVar=StringVar()
passwordVar=StringVar()
emailVar=StringVar()
confirm_passVar=StringVar()
#--------------------------------------------------------


#----------------- MAIN HEADING -------------------
def hotel_heading():
    header = CTkFrame(
        taz,
        height=70,
        corner_radius=0,
        fg_color="#1F6AA5"
    )
    header.pack(fill="x")

    # Heading
    heading = CTkLabel(
        header,
        text="Hotel Management System",
        font=("Arial", 28, "bold"),
        text_color="white"
    )
    heading.place(x=600,y=20)
hotel_heading()
#--------------------------------------------------------


#-------------------- Switch option---------------
def switch_option(switch_to):

    if switch_to=='login':
        signup_page_btn.configure(fg_color="gray", text_color="black")
        login_page_btn.configure(fg_color="#1F6AA5", text_color="white",border_color='white')

        for delete in page_frame.winfo_children():
            delete.destroy()
        login_page()

    elif switch_to=='signup':

        login_page_btn.configure(fg_color="gray", text_color="black",border_color='black')
        signup_page_btn.configure(fg_color="#1F6AA5", text_color='white',border_color='white')
        for delete in page_frame.winfo_children():
            delete.destroy()
        signup_page()
#--------------------------------------------------------



#----------------------- Creating a page frame for the login and signup-----------------------

page_frame=CTkFrame(master=taz,width=800,height=550,corner_radius=10)
page_frame.place(x=370,y=190)
#--------------------------------------------------------


#----------------- Login Button --------------------

login_page_btn=CTkButton(master=taz,text='Login',font=('Arial',20,'bold'),text_color='white',width=120,height=40,
                         corner_radius=10,border_width=2,
                         border_color='white',fg_color='#1F6AA5',command=lambda: switch_option(switch_to='login'))
login_page_btn.place(x=600,y=100)
#--------------------------------------------------------

#--------------------------Login Page ------------------------------
def login_page():
    signup_page_btn.configure(fg_color="gray")
    heading=CTkLabel(master=page_frame, text="Login Page",font=("Bahnschrift", 28, "bold"))
    heading.place(x=325,y=20)

    user_label = CTkLabel(master=page_frame, text="Username :", font=("Bahnschrift", 15, "bold"))
    user_label.place(x=200, y=155)
    username_entry=CTkEntry(master=page_frame,width=300,height=40,border_width=2,border_color='gray',corner_radius=10,
                            placeholder_text="Enter your username",textvariable=usernameVar)
    username_entry.place(x=300,y=150)

    pass_label = CTkLabel(master=page_frame, text="Password :", font=("Bahnschrift", 15, "bold"))
    pass_label.place(x=200, y=285)
    pass_entry = CTkEntry(master=page_frame, width=300, height=40, border_width=2, border_color='gray',corner_radius=10,
                          placeholder_text="Enter your password",show='*',textvariable=passwordVar)
    pass_entry.place(x=300, y=280)


    forgot_btn = CTkButton(master=page_frame, text='Forgot Password ?', font=('Arial', 15),fg_color='transparent',
                           hover=False)
    forgot_btn.place(x=310, y=340)
    CTkToolTip(forgot_btn,message="Forgot Password ?")

    agree_var =StringVar(value="off")
    checkbox =CTkCheckBox(master=page_frame, text="I agree to the Terms and Conditions",
                               variable=agree_var, onvalue="on", offvalue="off")
    checkbox.place(x=300, y=400)
    CTkToolTip(checkbox, message="Click to agree to the Terms and Conditions")


    #Message box for the login message
    def on_agree(variable, window):
        if variable.get() == "on" and username_entry.get() !='' and pass_entry.get() != '':
            if admin_login():
                welcome_page()
        elif username_entry.get() == '' and pass_entry.get() == '':
            messagebox.showwarning("Warning", "You must fill the username and password!")
        elif username_entry.get() == '':
            messagebox.showwarning("Warning", "You must fill the username!")
        elif pass_entry.get() == '':
            messagebox.showwarning("Warning", "You must fill the password!")
        elif variable.get() == "off":
            messagebox.showwarning("Warning", "You must agree to the terms to continue.")
    submit_button =CTkButton(page_frame, text="Agree and Continue",
                                  command=lambda: on_agree(agree_var,page_frame))
    submit_button.place(x=350, y=440)

#--------------------------------------------------------



#----------------- Signup Button --------------------

def otp_confirm_btn(confirm_otp):
    if confirm_otp == 'click':
        otp_entry = CTkEntry(master=page_frame, width=100, height=40, border_width=2, border_color='gray',
                               corner_radius=10, placeholder_text="Enter your otp")
        otp_entry.place(x=470, y=150)

signup_page_btn=CTkButton(master=taz,text='Sign-Up',font=('Arial',20,'bold'),text_color='white',width=120,height=40,
                          corner_radius=10,border_width=2,
                         border_color='white',fg_color='#1F6AA5',command=lambda: switch_option(switch_to='signup'))
signup_page_btn.place(x=800,y=100)
#--------------------------------------------------------


#----------------- Signup Page --------------------
def signup_page():
    heading=CTkLabel(master=page_frame, text="Signup Page",font=("Bahnschrift", 28, "bold"))
    heading.place(x=325,y=20)

    email_label = CTkLabel(master=page_frame, text="Email Address :", font=("Bahnschrift", 15, "bold"))
    email_label.place(x=170, y=105)
    email_entry=CTkEntry(master=page_frame,width=300,height=40,border_width=2,border_color='gray',corner_radius=10,
                         placeholder_text="Enter your E-mail address",textvariable=emailVar)
    email_entry.place(x=300,y=100)
    otp_btn = CTkButton(master=page_frame, text='Confirm your email', font=('Arial', 15), fg_color='gray',
                           hover_color=taz.cget("fg_color"),command=lambda: otp_confirm_btn('click'))

    otp_btn.place(x=310, y=155)
    CTkToolTip(otp_btn, message="Click to send the registration email!")

    user_label = CTkLabel(master=page_frame, text="Username :", font=("Bahnschrift", 15, "bold"))
    user_label.place(x=200, y=205)
    user_entry = CTkEntry(master=page_frame, width=300, height=40, border_width=2, border_color='gray',
                           corner_radius=10, placeholder_text="Create your username",textvariable=usernameVar)
    user_entry.place(x=300, y=200)

    pass_label = CTkLabel(master=page_frame, text="Password :", font=("Bahnschrift", 15, "bold"))
    pass_label.place(x=200, y=265)
    pass_entry = CTkEntry(master=page_frame, width=300, height=40, border_width=2, border_color='gray',corner_radius=10,
                          placeholder_text="Enter your password",show='*',textvariable=passwordVar)
    pass_entry.place(x=300, y=260)

    confirm_label = CTkLabel(master=page_frame, text="Confirm Password :", font=("Bahnschrift", 15, "bold"))
    confirm_label.place(x=140, y=325)
    confirm_entry = CTkEntry(master=page_frame, width=300, height=40, border_width=2, border_color='gray',
                          corner_radius=10, placeholder_text="Confirm Your password", show='*',textvariable=confirm_passVar)
    confirm_entry.place(x=300, y=320)

    agree_var =StringVar(value="off")
    checkbox =CTkCheckBox(master=page_frame, text="I agree to the Terms and Conditions",
                               variable=agree_var, onvalue="on", offvalue="off")
    checkbox.place(x=300, y=400)
    CTkToolTip(checkbox, message="Click to agree to the Terms and Conditions")


    #Message box for the login message
    def on_agree(variable, window):
        if variable.get() == "on" and email_entry.get() != '' and user_entry.get() !='' and pass_entry.get() != '' and confirm_entry.get() != '' and pass_entry.get()==confirm_entry.get():
            email=email_entry.get().strip()

            if not email.endswith('@gmail.com'):
                messagebox.showwarning("Warning", "The email must end's with @gmail.com.")
            else:
                info_insert()
        elif email_entry.get() == '':
            messagebox.showwarning("Warning", "Enter your email address!")
        elif confirm_entry.get() == '':
            messagebox.showwarning("Warning", "Confirm your password!")
        elif user_entry.get() == '':
            messagebox.showwarning("Warning", "You must create username!")
        elif pass_entry.get() == '':
            messagebox.showwarning("Warning", "You must fill the password!")
        elif variable.get() == "off":
            messagebox.showwarning("Warning", "You must agree to the terms to continue.")
        elif pass_entry.get() != confirm_entry.get():
            messagebox.showwarning("Warning", "Both password should be similar!!!")
    submit_button =CTkButton(page_frame, text="Agree and Register",command=lambda: on_agree(agree_var, page_frame))
    submit_button.place(x=350, y=440)

login_page()
#--------------------------------------------------------


#-------------- Signup data insert --------------------
def info_insert():
    db_config()
    username=usernameVar.get().strip()
    password=passwordVar.get()
    email=emailVar.get().strip().lower()
    que = "select * from user_info where binary user_name=%s or email_id=%s"
    val = (username, email)
    mycursor.execute(que, val)
    data=mycursor.fetchone()
    print(data)

    if data == None:
        que = "insert into user_info (email_id,user_name,pass_id) values(%s,%s,%s)"
        value = (email, username, password)
        mycursor.execute(que, value)
        connection.commit()
        messagebox.showinfo("Success", "User successfully registered!")
        for data1 in page_frame.winfo_children():
            data1.destroy()
        login_page()
        signup_page_btn.configure(fg_color="gray", text_color="black")
        login_page_btn.configure(fg_color="#1F6AA5", text_color="white", border_color='white')
    else:
        messagebox.showerror("Error","The e-mail or username is already in use!")
#--------------------------------------------------------


#--------Admin Login--------

def admin_login():
    db_config()
    username=usernameVar.get()
    password = passwordVar.get()

    que = "select * from user_info where binary email_id=%s or user_name=%s and pass_id=%s"
    val = (username,username,password)
    mycursor.execute(que, val)
    data = mycursor.fetchone()
    if data != None:
        for data in taz.winfo_children():
            data.destroy()
        return True
    else:
        messagebox.showerror("Error","Either the username or password is incorrect")
#--------------------------------------------------------


#------------------------- WELCOME PAGE -------------------------------
def welcome_page():
    hotel_heading()


#--------------------------------------------------------


#------------------------ Main component--------------------------------
login_page()
taz.after(100, lambda: taz.state("zoomed"))
taz.mainloop()
#--------------------------------------------------------