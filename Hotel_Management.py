from click import command
from customtkinter import *
from tkinter import messagebox #Imported to display some warnings
from CTkToolTip import CTkToolTip #Imported for the hover message
import pymysql
from PIL import Image, ImageTk
from unicodedata import category


#------------- Data Base for the SQL -------------------
def db_config():
    global mycursor
    global connection
    connection = pymysql.connect(user="root", host="127.0.0.1", database="hotel_db")
    mycursor = connection.cursor()
#--------------------------------------------------------


#------------------- Custom Tkinter ----------------------
menu_frame=None
taz=CTk()
taz.title("Hotel Management System")
#--------------------------------------------------------

#------------------------ Data Base Variable--------------------------------
#------------------------- Info Variable-------------------------------

usernameVar=StringVar()
passwordVar=StringVar()
emailVar=StringVar()
confirm_passVar=StringVar()
#------------------------ Item insert var--------------------------------

itemnameVar=StringVar()
hpriceVar=StringVar()
fpriceVar=StringVar()
selectOptionVar=StringVar()

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
    heading.place(relx=0.5,rely=0.5,anchor="center")

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
def login_frame():
    global page_frame
    page_frame = CTkFrame(master=taz, width=800, height=550, corner_radius=10)
    page_frame.place(relx=0.5, rely=0.55, anchor="center")


#--------------------------------------------------------


#----------------- Login Button --------------------

def login_sign():
    global login_page_btn,signup_page_btn
    login_page_btn = CTkButton(master=taz, text='Login', font=('Arial', 20, 'bold'), text_color='white', width=120,
                               height=40,
                               corner_radius=10, border_width=2,
                               border_color='white', fg_color='#1F6AA5',
                               command=lambda: switch_option(switch_to='login'))
    login_page_btn.place(relx=0.45, rely=0.148, anchor="center")

    signup_page_btn = CTkButton(master=taz, text='Sign-Up', font=('Arial', 20, 'bold'), text_color='white', width=120,
                                height=40,
                                corner_radius=10, border_width=2,
                                border_color='white', fg_color='#1F6AA5',
                                command=lambda: switch_option(switch_to='signup'))
    signup_page_btn.place(relx=0.58, rely=0.148, anchor="center")


#--------------------------------------------------------

#--------------------------Login Page ------------------------------
def login_page():
    hotel_heading()
    login_sign()
    login_frame()
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
    def on_agree(variable):
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
                                  command=lambda: on_agree(agree_var))
    submit_button.place(x=350, y=440)

#--------------------------------------------------------



#----------------- Signup Button --------------------

def otp_confirm_btn(confirm_otp):
    if confirm_otp == 'click':
        otp_entry = CTkEntry(master=page_frame, width=100, height=40, border_width=2, border_color='gray',
                               corner_radius=10, placeholder_text="Enter your otp")
        otp_entry.place(x=470, y=150)


#--------------------------------------------------------


#----------------- Signup Page --------------------
def signup_page():
    login_sign()
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
    def on_agree(variable):
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
    submit_button =CTkButton(page_frame, text="Agree and Register",command=lambda: on_agree(agree_var))
    submit_button.place(x=350, y=440)


#--------------------------------------------------------

#----------------------- Menu Show Page---------------------------------

def welcome_page():
    for data in taz.winfo_children():
        data.destroy()

    hotel_heading()
    menu_page()

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

    if data == None:
        que = "insert into user_info (email_id,user_name,pass_id) values(%s,%s,%s)"
        value = (email, username, password)
        mycursor.execute(que, value)
        connection.commit()
        messagebox.showinfo("Success", "User successfully registered!")
        for data1 in taz.winfo_children():

            data1.destroy()
        usernameVar.set("")
        passwordVar.set("")
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
        usernameVar.set('')
        passwordVar.set('')
        return True
    else:
        messagebox.showerror("Error","Either the username or password is incorrect")
    usernameVar.set('')
    passwordVar.set('')
#--------------------------------------------------------


#------------------------- WELCOME PAGE -------------------------------
def menu_page():
    # hotel_heading()
    global menu_btn
    menu_btn=CTkButton(master=taz,text='Menu',width=50,height=50,border_color='white',fg_color='transparent',hover_color='#383838',
                       command=menu_frames)
    menu_btn.place(x=10,y=80)

#--------------------------------------------------------

#-------------------------- Logout section------------------------------
def logout_btn():
    for data in taz.winfo_children():
        data.destroy()
    menu_btn.destroy()
    hide_menu_frame()
    login_page()
#--------------------------------------------------------

#--------------------------- Menu Frame-----------------------------
def hide_menu_frame():
    if menu_frame is not None and menu_frame.winfo_exists():
        menu_frame.pack_forget()

def menu_frames():

    global menu_frame

    if menu_frame is not None and menu_frame.winfo_exists():
        menu_frame.pack(
            side="left",
            fill="y",
            padx=15,
            pady=15
        )
        return


    menu_frame = CTkFrame(master=taz, width=300, height=790,corner_radius=20)
    menu_frame.pack(side="left",fill='y',padx=15,pady=15)



    menu_exbtn = CTkButton(master=menu_frame, text='exit', width=25, height=25, border_color='white',
                           fg_color='transparent',
                           hover_color='#383838',
                           command=hide_menu_frame)
    menu_exbtn.place(x=15, y=20)


    account_frame=CTkFrame(master=menu_frame, width=280, height=150,fg_color="#383838",corner_radius=10)
    account_frame.grid(row=0,column=0, padx=15,pady=50)
    photo_frame=CTkFrame(master=account_frame,width=100,height=100,corner_radius=100)
    photo_frame.place(x=10,y=10)


    btn_frame = CTkFrame(master=menu_frame, width=260, height=450, corner_radius=20)
    btn_frame.grid(row=1,column=0,padx=15,pady=15)

    btn_frame_label = CTkLabel(master=btn_frame, text="| Your Preferences",font=('Microsoft JhengHei',15,'bold'),fg_color="#404040",text_color="#81C784")
    btn_frame_label.grid(row=1,column=0,pady=15)


    add_food=CTkButton(master=btn_frame,text="Add item to the menu",width=260,font=('Microsoft YaHei UI',15),hover_color='#303030',
                       fg_color='transparent',command=insert_food)
    add_food.grid(row=2,column=0,pady=15)

    view_order = CTkButton(master=btn_frame, text="See the order", width=260, font=('Microsoft YaHei UI', 15),
                         hover_color='#303030', fg_color='transparent')
    view_order.grid(row=3, column=0, pady=15)

    view_emp = CTkButton(master=btn_frame, text="See the Employees", width=260, font=('Microsoft YaHei UI', 15),
                           hover_color='#303030', fg_color='transparent')
    view_emp.grid(row=4, column=0, pady=15)

    home_page = CTkButton(master=btn_frame, text="Home Page", width=260, font=('Microsoft YaHei UI', 15),
                         hover_color='#303030', fg_color='transparent',command=welcome_page)
    home_page.grid(row=5, column=0, pady=15)

    #Accessebility

    more_frame = CTkFrame(master=menu_frame, width=260, height=450, corner_radius=20)
    more_frame.grid(row=2, column=0, padx=15, pady=15)

    acc_label = CTkLabel(master=more_frame, text="| More", font=('Microsoft JhengHei', 15, 'bold'),
                               fg_color="#404040", text_color="#81C784")
    acc_label.grid(row=1, column=0, pady=15)

    # setting_btn = CTkButton(master=more_frame, text="Setting", width=260, font=('Microsoft YaHei UI', 15),
    #                      hover_color='#303030',
    #                      fg_color='transparent')
    # setting_btn.grid(row=2, column=0, pady=15)

    log_out = CTkButton(master=more_frame, text="Log-out", width=260, font=('Microsoft YaHei UI', 15),
                           hover_color='#303030', fg_color='transparent',command=logout_btn)
    log_out.grid(row=2, column=0, pady=15)
#--------------------------------------------------------

#------------------------- Insert DB-------------------------------
def insertFood_db():
    db_config()
    itemname=itemnameVar.get()
    itemhprice=int(hpriceVar.get())
    itemfprice=int(fpriceVar.get())
    itemcategory=selectOptionVar.get()

    query="insert into item_info (item_name,half_price,full_price,category) values(%s,%s,%s,%s)"
    value=(itemname,itemhprice,itemfprice,itemcategory)
    mycursor.execute(query,value)
    connection.commit()
    messagebox.showinfo("Success", "Item inserted successfully")

    itemnameVar.set("")
    hpriceVar.set("")
    fpriceVar.set("")
    selectOptionVar.set("Select food type")


#--------------------------------------------------------
#-------------------------- Insert Item ------------------------------

def insert_food():
    for data in taz.winfo_children():
        data.destroy()
    menu_frame=None
    welcome_page()
    page_frame = CTkFrame(master=taz, width=800, height=550, corner_radius=10)
    page_frame.place(relx=0.5, rely=0.55, anchor="center")

    heading = CTkLabel(master=page_frame, text="Insert Item", font=("Bahnschrift", 28, "bold"))
    heading.place(x=325, y=20)

    item_label = CTkLabel(master=page_frame, text="Add Item :", font=("Bahnschrift", 15, "bold"))
    item_label.place(x=210, y=105)
    item_entry = CTkEntry(master=page_frame, width=300, height=40, border_width=2, border_color='gray',
                           corner_radius=10,
                           placeholder_text="Enter the food name", textvariable=itemnameVar)
    item_entry.place(x=300, y=100)

    hprice_label = CTkLabel(master=page_frame, text="Half Price :", font=("Bahnschrift", 15, "bold"))
    hprice_label.place(x=200, y=205)
    hprice_entry = CTkEntry(master=page_frame, width=300, height=40, border_width=2, border_color='gray',
                          corner_radius=10, placeholder_text="Enter price of half", textvariable=hpriceVar)
    hprice_entry.place(x=300, y=200)

    fprice_label = CTkLabel(master=page_frame, text="Full Price :", font=("Bahnschrift", 15, "bold"))
    fprice_label.place(x=200, y=265)
    fprice_entry = CTkEntry(master=page_frame, width=300, height=40, border_width=2, border_color='gray',
                          corner_radius=10,
                          placeholder_text="Enter price of full", textvariable=fpriceVar)
    fprice_entry.place(x=300, y=260)

    category_label = CTkLabel(master=page_frame, text="Category :", font=("Bahnschrift", 15, "bold"))
    category_label.place(x=200, y=325)

    categoryVar=StringVar(value="Select food type")

    category_entry = CTkOptionMenu(master=page_frame, values=["Indian", "Chinese", "South Indian", "Beverages", "Desert", "Pizza"],
                                   font=("Bahnschrift", 15, "bold"), width=200, height=40,fg_color="#303030",
                                   dropdown_hover_color="#303030",variable=categoryVar)

    category_entry.place(x=300, y=325)


    def insert_agree():
        global selectOptionVar
        selectOptionVar.set(categoryVar.get())
        if selectOptionVar.get()!="Select food type" and item_entry.get() !='' and hprice_entry.get() !='' and fprice_entry.get() !='' and int(hprice_entry.get()) < int(fprice_entry.get()):
            insertFood_db()

        elif item_entry.get() == '':
            messagebox.showwarning("Warning", "Enter the item name!")
        elif hpriceVar.get() == '':
            messagebox.showwarning("Warning", "Initialize the half price!")
        elif fprice_entry.get() == '':
            messagebox.showwarning("Warning", "Initialize the full price!")
        elif selectOptionVar.get() == "Select food type":
            messagebox.showwarning("Warning", "Choose the food category!")


    submit_button = CTkButton(page_frame, text="Agree and Register", command=lambda: insert_agree())
    submit_button.place(x=350, y=440)


#--------------------------------------------------------

#------------------------ Main component--------------------------------
login_page()

# menu_frames()
taz.after(100, lambda: taz.state("zoomed"))
taz.mainloop()
#--------------------------------------------------------