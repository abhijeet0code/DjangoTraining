from tkinter import *

root=Tk()
root.title("Windows Calculator") #Title for the window
def msg():
    print("You clicked the button")
#To print the value of the name

#The geometry size for the calculator
root.geometry("900x700+100+20")
#To set the icon for the windows
root.wm_iconbitmap("login.ico")
lbl=Label(root,text="Enter first number :-",
          font=("Comic Sans Ms", 15, "bold"), fg="gray")
lbl.place(x=50,y=50)
#Name variable
name=StringVar()
entry=Entry(root,textvariable=name)
entry.pack(padx=5, pady=60)
def showName():
    print(name.get())

button = Button(root, text="Submit", command=showName)
button.pack()


root.mainloop()