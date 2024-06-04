#import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import os
from DTO.Varios import hash_md5

def Login():# Esta función se ejecutará cuando se presione el botón

    # vamos a ocultar la ventana principal
    root.withdraw()

    # crear nueva ventana para el Login
    login_window = Toplevel(root)
    login_window.title("Log In")
    login_window.geometry("400x450")
    login_window.config(bg="white")

    Frame_up = Frame(login_window, width=400, height=70, bg="white")
    Frame_up.grid(row=0, column=0)

    Frame_down = Frame(login_window, width=400, height=380, bg="white")
    Frame_down.grid(row=1, column=0)

    def return_principal():
        print("Return Principal")

    # declaring string variable
    # for storing name and password
    Email_var = StringVar()
    passw_var = StringVar()
    def Help_function():
        print("Help")
    # defining a function that will
    # get the name and password and
    # print them on the screen
    def submit():

        Email = Email_var.get()
        password = passw_var.get()
        if len(Email) == 0:
            messagebox.showinfo("Warning", "Please fill the email field")
        elif len(password) == 0:
            messagebox.showinfo("Warning", "Please fill the password field")
        else:
            Email = Email_var.get()
            password = hash_md5(passw_var.get())
            print(Email)
            print(password)



    def Forgot_password():
        print("forgot password")


    Header = Label(Frame_up, text="LOGIN", font=('Poppins', 23, "bold"), bg="white").place(x=40, y=20)

    line = Label(Frame_up, width=40, text="", height=1, bg="#3fb5a3", anchor=NW)
    line.place(x=35, y=65)

    Email_label = Label(Frame_down, text='Email',font=('calibre', 11, 'bold'), bg="white").place(x=70, y=45)

    Email_entry = Entry(Frame_down,
                       textvariable=Email_var,
                       font=('calibre', 17, 'normal'),
                       bg="white",
                       borderwidth=2,
                       width=20).place(x=55, y=70)
    #if name_entry=='':

    #   creating a label for password
    passw_label = Label(Frame_down, text='Password', font=('calibre', 11, 'bold'), bg="white").place(x=65, y=118)
    pass_F = Button(Frame_down,
                    text='Forgot Password',
                    command=Forgot_password,
                    font=('calibre', 9, 'bold'),
                    activebackground="White",
                    activeforeground="#4641FF",
                    bg="white",
                    fg="#0800FF",
                    highlightthickness = 0,
                    bd = 0).place(x=200, y=120)

    # creating an entry for password
    passw_entry = Entry(Frame_down,
                        textvariable=passw_var,
                        font=('calibre', 17, 'normal'),
                        show='*',
                        borderwidth=2,
                        bg="white",
                        width=20).place(x=55, y=145)

    # creating a button using the widget
    # Button that will call the submit function
    sub_btn = Button(Frame_down,
                    text='Submit',
                    font=('calibre', 10, 'bold'),
                    width=15,
                    bg="#3fb5a3",
                    fg="white",
                    activebackground="#47DFC8",
                    activeforeground="white",
                    command=submit).place(x=125, y=195)

    return_btn = Button(Frame_down,
                    text='return',
                    font=('calibre', 10, 'bold'),
                    width=10,
                    bg="#3fb5a3",
                    fg="white",
                    activebackground="#47DFC8",
                    activeforeground="white",
                    command=return_principal).place(x=35, y=320)

    help_btn = Button(Frame_down,
                        text=' Help? ',
                        font=('calibre', 10, 'bold'),
                        width=8,
                        bg="#3fb5a3",
                        fg="white",
                        activebackground="#47DFC8",
                        activeforeground="white",
                        command=Help_function).place(x=305, y=320)


def Sign_up():
    root.withdraw()
    Sign_up_window = Toplevel(root)
    Sign_up_window.title("Sign up")
    Sign_up_window.minsize(width=600, height=400)

def User_interface():
    # vamos a ocultar la ventana principal
    login_window.withdraw()

    # crear nueva ventana para el Login
    User_interface = Toplevel(login_window)
    User_interface.title("User_interface")
    User_interface.geometry("400x450")
    User_interface.config(bg="white")

# crear ventana principal de la interfaz
root = Tk()
# agegarle un nombre a la ventana
root.title("menu principal")
# ajustar el tamaño de la ventana
root.minsize(width=300, height=250)
# agregar relleno a los lados de la ventana principal
root.config(padx=30, pady=30)

# Colocar un botón en la interfaz con el nombre 'Login'
boton_Login = Button(root,
                        text="Login",
                        command=Login,
                        width=10,
                        height=2,
                        font=("Arial", 12),
                        cursor="hand2",
                        justify="center",
                        padx=10,
                        pady=5
                        )
# agregar el boton a la ventana principal
boton_Login.pack(padx=20, pady=20)

# Creando un botón en la interfaz con el nombre 'Sign up'
boton_Sign_up = Button(root,
                        text="Sign up",
                        command=Sign_up,
                        width=10,
                        height=2,
                        font=("Arial", 12),
                        cursor="hand2",
                        justify="center",
                        padx=10,
                        pady=5
                        )
# agregar el boton a la ventana principal
boton_Sign_up.pack(padx=20, pady=20)

root.mainloop()