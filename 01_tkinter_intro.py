from tkinter import *

root=Tk()
root.title("Windows Calculator") #Title for the window
def msg():
    print("You clicked the button")
#The geometry size for the calculator
root.geometry("400x600+100+100")
#To set the icon for the windows
root.wm_iconbitmap("calci.ico")

#Creating a button1
btn1=Button(root,text="%",command=msg,font=("Arial",20,),bg="gray",fg="black")
btn1.place(x=20,y=520) # % button
btn2=Button(root,text="0",command=msg,font=("Arial",20,),bg="gray",fg="black")
btn2.place(x=120,y=520) # 0 button
btn3=Button(root,text=".",command=msg,font=("Arial",20,),bg="gray",fg="black")
btn3.place(x=220,y=520) # . button
btn4=Button(root,text="=",command=msg,font=("Arial",20,),bg="blue",fg="black")
btn4.place(x=320,y=520) # = button (Main calculation button)'
#Bottom level is completed

btn5=Button(root,text="%",command=msg,font=("Arial",20,),bg="gray",fg="black")
btn5.place(x=20,y=520) # % button
btn6=Button(root,text="0",command=msg,font=("Arial",20,),bg="gray",fg="black")
btn6.place(x=120,y=520) # 0 button
btn3=Button(root,text=".",command=msg,font=("Arial",20,),bg="gray",fg="black")
btn3.place(x=220,y=520) # . button
btn5=Button(root,text="+",command=msg,font=("Arial",20,),bg="white",fg="black")
btn5.place(x=320,y=440) # + button
btn6=Button(root,text="-",command=msg,font=("Arial",20,),bg="white",fg="black")
btn6.place(x=320,y=360) # - button
btn7=Button(root,text="x",command=msg,font=("Arial",20,),bg="white",fg="black")
btn7.place(x=320,y=280) # x button
btn5=Button(root,text="/",command=msg,font=("Arial",20,),bg="white",fg="black")
btn5.place(x=320,y=200) # / button

root.mainloop()