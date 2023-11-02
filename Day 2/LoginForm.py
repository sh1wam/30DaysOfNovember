import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Login Form")
window.geometry('340x440')
window.configure(bg='#333333')

def login():
    username = "Shiwam"
    pasword = "12345"
    if username_entry.get()==username and password_entry.get()==pasword:
        messagebox.showinfo(title="Login Success", message="Successfully Logged In!")
    else:
        messagebox.showerror(title="Error", message="Invalid Login!")

frame = tkinter.Frame(bg='#333333')

#Creating Widgets
login_label = tkinter.Label(frame, text="Login", bg='#333333', fg='#ff3399', font=("Arial", 30))
username_label = tkinter.Label(frame, text="Username", bg='#333333', fg='#ffffff', font=("Arial", 15))
username_entry = tkinter.Entry(frame, font=("Arial", 15))
password_label = tkinter.Label(frame, text="Password", bg='#333333', fg='#ffffff', font=("Arial", 15))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 15))
login_button = tkinter.Button(frame, text="login", bg='#ff3399', fg='#ffffff', font=("Arial", 16), command=login)

#Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=30)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=10)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=10)
login_button.grid(row=3, column=0, columnspan=2, pady=10)

frame.pack()
window.mainloop()