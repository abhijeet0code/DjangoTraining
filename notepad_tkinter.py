from tkinter import *
from tkinter import filedialog, messagebox

root = Tk()
root.title("My Notepad")
root.geometry("800x550")
root.config(bg="#202020")

file_path = ""

def new_file():
    global file_path
    text_area.delete("1.0", END)
    file_path = ""
    root.title("My Notepad - New File")

def open_file():
    global file_path

    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        file = open(file_path, "r")
        data = file.read()
        file.close()
        text_area.delete("1.0", END)
        text_area.insert("1.0", data)

        root.title("My Notepad - " + file_path)

def save_file():
    global file_path

    if file_path == "":
        save_as_file()
    else:
        file = open(file_path, "w")
        data = text_area.get("1.0", END)
        file.write(data)
        file.close()
        messagebox.showinfo("Saved", "File Saved Successfully")
def save_as_file():
    global file_path
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"),
        ("All Files", "*.*")]
    )
    if file_path:
        file = open(file_path, "w")
        data = text_area.get("1.0", END)
        file.write(data)
        file.close()

        root.title("My Notepad - " + file_path)
        messagebox.showinfo("Saved", "File Saved Successfully")

main_menu = Menu(root)
root.config(menu=main_menu)

top_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="File", menu=top_menu)

top_menu.add_command(label="New", accelerator="Ctrl+N", command=new_file)
top_menu.add_command(label="Open", accelerator="Ctrl+O", command=open_file)
top_menu.add_separator()
top_menu.add_command(label="Save", accelerator="Ctrl+S", command=save_file)
top_menu.add_command(label="Save As", command=save_as_file)
top_menu.add_separator()
top_menu.add_command(label="Exit", command=root.destroy)

editMenu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="Edit", menu=editMenu)

editMenu.add_command(label="Cut", command=lambda: text_area.event_generate("<<Cut>>"))
editMenu.add_command(label="Copy", command=lambda: text_area.event_generate("<<Copy>>"))
editMenu.add_command(label="Paste", command=lambda: text_area.event_generate("<<Paste>>"))
helpMenu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About",command=lambda: messagebox.showinfo("About", "Simple Notepad using Tkinter"))
button_frame = Frame(root, bg="#202020")
button_frame.pack(pady=5)

new_button = Button(button_frame, text="New", width=10, command=new_file)
new_button.pack(side=LEFT, padx=5)
open_button = Button(button_frame, text="Open", width=10, command=open_file)
open_button.pack(side=LEFT, padx=5)
save_button = Button(button_frame, text="Save", width=10, command=save_file)
save_button.pack(side=LEFT, padx=5)
save_as_button = Button(button_frame, text="Save As", width=10, command=save_as_file)
save_as_button.pack(side=LEFT, padx=5)

text_area = Text(root,font=("Consolas", 16),bg="#2b2b2b",fg="white",insertbackground="white",wrap=WORD)
text_area.pack(padx=10, pady=10, fill=BOTH, expand=True)

root.mainloop()