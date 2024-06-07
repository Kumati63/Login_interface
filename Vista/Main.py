#import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import Canvas
from PIL import ImageTk, Image
import random
import pymysql
import os
from DTO.Varios import hash_md5


def menu_usuario():
    login_window.withdraw()

    Menu_usu = Toplevel()
    Menu_usu.title("Menu Usuario")
    Menu_usu.minsize(width=400, height=200)
    Menu_usu.config(padx=30, pady=30)

    # Botón para abrir ventana ingreso sintomas
    Button(Menu_usu, text="ingresar sintomas").pack(pady=10)

    # Botón para abrir ventana ingreso virus
    Button(Menu_usu, text="ingresar virus").pack(pady=10)

    # Botón para abrir ventana ingreso de ADN
    Button(Menu_usu, text="Ingresar ADN").pack(pady=10)

    # Botón para salir de la ventana secundaria
    Button(Menu_usu, text="Salir del Usuario").pack(pady=10)

def Login():# Esta función se ejecutará cuando se presione el botón

    def verificar_credenciales():
        Email_usu = Email_var.get()
        password_usu = hash_md5(passw_var.get())

        conexion = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='login_interface'
        )
        cursor = conexion.cursor()

        cursor.execute("SELECT email, password FROM usuario WHERE email = %s AND password = %s",
                       (Email_usu, password_usu))

        usuario = cursor.fetchone()

        print("--------------------------------")
        print(Email_usu)
        print(password_usu)
        conexion.close()

        if usuario:
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
            menu_usuario()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    # vamos a ocultar la ventana principal
    root.withdraw()

    ventana_registro.withdraw()
    # crear nueva ventana para el Login
    global login_window
    login_window = Toplevel(root)
    login_window.title("Log In")
    login_window.geometry("800x450")
    login_window.config(bg="white")

    Frame_left = Frame(login_window, width=400, height=430, bg="white")
    Frame_left.grid(row=0, column=0)

    Frame_right = Frame(login_window, width=400, height=430, bg="white")
    Frame_right.grid(row=0, column=1)

    Frame_up = Frame(Frame_right, width=400, height=70, bg="white")
    Frame_up.grid(row=0, column=1)

    Frame_down = Frame(Frame_right, width=400, height=380, bg="white")
    Frame_down.grid(row=1, column=1)

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
            verificar_credenciales()



    def Forgot_password():
        recuperar_contra()

    # Step 3: Load the image using PIL
    image_path = image_path = os.path.join(os.path.dirname(__file__), '..', 'img', 'newimage.png')  # Replace with your image path
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    # Step 4: Create a Canvas widget and add the image to it
    canvas = Canvas(Frame_left, width=400, height=400)
    canvas.pack()

    # Add the image to the canvas
    canvas.create_image(0, 0, anchor=NW, image=photo)

    # Keep a reference to avoid garbage collection
    canvas.image = photo

    Header = Label(Frame_up, text="LOGIN", font=('Poppins', 23, "bold"), bg="white").place(x=40, y=20)

    line = Label(Frame_up, width=40, text="", height=1, bg="#007dfe", anchor=NW)
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
                    bg="#007dfe",
                    fg="white",
                    activebackground="#1E78D5",
                    activeforeground="white",
                    command=submit).place(x=125, y=195)

    return_btn = Button(Frame_down,
                    text='return',
                    font=('calibre', 10, 'bold'),
                    width=10,
                    bg="#007dfe",
                    fg="white",
                    activebackground="#1E78D5",
                    activeforeground="white",
                    command=return_to_main_from_login).place(x=35, y=320)

    help_btn = Button(Frame_down,
                    text=' Help? ',
                    font=('calibre', 10, 'bold'),
                    width=8,
                    bg="#007dfe",
                    fg="white",
                    activebackground="#1E78D5",
                    activeforeground="white",
                    command=Help_function).place(x=305, y=320)

def return_to_main_from_login():
    login_window.withdraw()
    root.deiconify() #restaurar la ventana principal

def return_to_main_from_signup():
    ventana_registro.withdraw()
    root.deiconify() #restaurar la ventana principal

def return_to_login():
    ventana_registro.withdraw()
    root.deiconify()

def cambiar_contra():
    root.withdraw()
    ventana = Toplevel(root)
    ventana.title("Recuperación de Contraseña")
    ventana.geometry("650x450")
    ventana.configure(bg="white")

    def validate_length(new_value):
        max_length = 25
        if len(new_value) > max_length:
            return False
        return True
    # Registra la función de validación
    validate_cmd = ventana.register(validate_length)

    def validar_contraseña():
        password1 = password.get()
        password2 = password2_pass.get()

        if password1 != password2:
            messagebox.showwarning("Advertencia", "Las contraseñas no coinciden")
            return False
        else:
            return True

    def boton_guardar():
        if validar_contraseña():
            # info para almacenar en bd
            messagebox.showinfo("Creación de Usuario", "Datos almacenados con éxito")

    frame_cabecera = Frame(ventana, bg="white")
    frame_cabecera.grid(row=0, column=1, columnspan=1, padx=10, pady=20)
    cabecera = Label(frame_cabecera, text="Recuperacion de contraseña", font=('Poppins', 18, "bold"), bg="white",
                        anchor="center")
    cabecera.pack()

    """line = Label(ventana, width=30, text="", height=1, bg="#3fb5a3", anchor=NW)
    line.grid(row=1, column=1, columnspan=1, padx=10, pady=5)"""

    frame_contenido = Frame(ventana, bg="white")
    frame_contenido.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Etiquetas y campos de entrada dentro del frame de contenido

    password_label = Label(frame_contenido, text="CONTRASEÑA", font=('calibre', 11, 'bold'), bg="white")
    password_label.grid(row=0, column=0, padx=30, pady=10, sticky="e")
    password = Entry(frame_contenido, width=25, show="*", validate="key", validatecommand=(validate_cmd, '%P'),font=('calibre', 17, 'normal'), bg="white", borderwidth=2)
    password.grid(row=0, column=1, padx=10, pady=10)

    password2_label = Label(frame_contenido, text="REPETIR CONTRASEÑA", font=('calibre', 11, 'bold'), bg="white")
    password2_label.grid(row=1, column=0, padx=30, pady=10, sticky="e")
    password2_pass = Entry(frame_contenido, width=25, show="*", validate="key", validatecommand=(validate_cmd, '%P'),font=('calibre', 17, 'normal'), bg="white", borderwidth=2)
    password2_pass.grid(row=1, column=1, padx=10, pady=10)

    boton = Button(frame_contenido, text="verificar", font=('calibre', 10, 'bold'), width=15, bg="#1E78D5",fg="white", activebackground="#1E78D5", activeforeground="white", command=boton_guardar)
    boton.grid(row=2, column=1, padx=1, pady=20)
def recuperar_contra():
    root.withdraw()
    ventana = Toplevel(root)
    ventana.title("Recuperación de Contraseña")
    ventana.geometry("650x450")
    ventana.configure(bg="white")

    def validate_length(new_value):
        max_length = 25
        if len(new_value) > max_length:
            return False
        return True

    def boton_codigo():
        reset_code = random.randint(100000, 999999)
        print(reset_code)
        messagebox.showinfo("Código de Recuperación", "Código enviado con éxito")

    # Registra la función de validación
    validate_cmd = ventana.register(validate_length)

    frame_cabecera = Frame(ventana, bg="white")
    frame_cabecera.grid(row=0, column=1, columnspan=1, padx=10, pady=20)
    cabecera = Label(frame_cabecera, text="Recuperación de Contraseña", font=('Poppins', 18, "bold"), bg="white", anchor="center")
    cabecera.pack()

    frame_contenido = Frame(ventana, bg="white")
    frame_contenido.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Etiquetas y campos de entrada dentro del frame de contenido
    correo_label = Label(frame_contenido, text="CORREO", font=('calibre', 11, 'bold'), bg="white")
    correo_label.grid(row=0, column=0, padx=30, pady=10, sticky="e")
    correo = Entry(frame_contenido, width=25, validate="key", validatecommand=(validate_cmd, '%P'), font=('calibre', 17, 'normal'), bg="white", borderwidth=2, state="disabled")
    correo.grid(row=0, column=1, padx=10, pady=10)

    boton1 = Button(frame_contenido, text="Enviar Código", font=('calibre', 10, 'bold'), width=15, bg="#1E78D5", fg="white", activebackground="#1E78D5", activeforeground="white", command=boton_codigo)
    boton1.grid(row=1, column=1, padx=1, pady=20)

    usuario_label = Label(frame_contenido, text="INGRESAR CÓDIGO", font=('calibre', 11, 'bold'), bg="white")
    usuario_label.grid(row=2, column=0, padx=30, pady=10, sticky="e")
    usuario = Entry(frame_contenido, width=25, validate="key", validatecommand=(validate_cmd, '%P'), font=('calibre', 17, 'normal'), bg="white", borderwidth=2)
    usuario.grid(row=2, column=1, padx=10, pady=10)

    boton2 = Button(frame_contenido, text="Verificar Código", font=('calibre', 10, 'bold'), width=15, bg="#1E78D5", fg="white", activebackground="#1E78D5", activeforeground="white", command = return_to_main_from_signup)
    boton2.grid(row=3, column=1, padx=1, pady=20)
def Sign_up():
    root.withdraw()
    global ventana_registro
    ventana_registro = Toplevel(root)
    ventana_registro.title("Sign up")
    ventana_registro.geometry("650x450")
    ventana_registro.configure(bg="white")

    def validate_length(new_value):
        max_length = 25
        if len(new_value) > max_length:
            return False
        return True

    def validar_contraseña():
        password1 = password_var.get()
        password2 = password2_pass_var.get()

        if password1 != password2:
            messagebox.showwarning("Advertencia", "Las contraseñas no coinciden")
            return False
        else:
            return True

    usuario_var = StringVar()
    password_var = StringVar()
    correo_var = StringVar()
    password2_pass_var = StringVar()

    def boton_guardar():
        if validar_contraseña():
            usuario = usuario_var.get()
            correo = correo_var.get()
            password = password_var.get()
            password2_pass = password2_pass_var.get()

            if len(usuario) == 0:
                messagebox.showinfo("Warning", "por favor llenar el campo: usuario")
            elif len(correo) == 0:
                messagebox.showinfo("Warning", "por favor llenar el campo: correo")
            elif len(password) == 0:
                messagebox.showinfo("Warning", "Por favor llenar el campo: contraseña")
            elif len(password2_pass) == 0:
                messagebox.showinfo("Warning", "por favor llenar el campo: repetir contraseña")
            else:
                password_hash = hash_md5(password)
                print(password_hash)
                print(usuario)
                print(correo)
                print(password)
                print(password2_pass)

                messagebox.showinfo("Creación de Usuario", "Datos almacenados con éxito")
                Login()

    # Registra la función de validación
    validate_cmd = ventana_registro.register(validate_length)

    frame_cabecera = Frame(ventana_registro, bg="white")
    frame_cabecera.grid(row=0, column=1, columnspan=1, padx=10, pady=10)
    cabecera = Label(frame_cabecera, text="Introduzca los datos solicitados", font=('Poppins', 18, "bold"), bg="white",anchor="center")
    cabecera.pack()

    """line = Label(ventana, width=30, text="", height=1, bg="#3fb5a3", anchor=NW)
    line.grid(row=1, column=1, columnspan=1, padx=10, pady=5)"""

    frame_contenido = Frame(ventana_registro, bg="white")
    frame_contenido.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Etiquetas y campos de entrada dentro del frame de contenido
    usuario_label = Label(frame_contenido, text="USUARIO", font=('calibre', 11, 'bold'), bg="white")
    usuario_label.grid(row=0, column=0, padx=30, pady=10, sticky="e")
    usuario = Entry(frame_contenido, width=25, validate="key", textvariable=usuario_var,validatecommand=(validate_cmd, '%P'), font=('calibre', 17, 'normal'), bg="white", borderwidth=2)
    usuario.grid(row=0, column=1, padx=10, pady=10)

    correo_label = Label(frame_contenido, text="CORREO", font=('calibre', 11, 'bold'), bg="white")
    correo_label.grid(row=1, column=0, padx=30, pady=10, sticky="e")
    correo = Entry(frame_contenido, width=25, validate="key", textvariable=correo_var,validatecommand=(validate_cmd, '%P'), font=('calibre', 17, 'normal'), bg="white", borderwidth=2)
    correo.grid(row=1, column=1, padx=10, pady=10)

    password_label = Label(frame_contenido, text="CONTRASEÑA", font=('calibre', 11, 'bold'), bg="white")
    password_label.grid(row=2, column=0, padx=30, pady=10, sticky="e")
    password = Entry(frame_contenido, width=25, show="*", validate="key", textvariable=password_var,validatecommand=(validate_cmd, '%P'), font=('calibre', 17, 'normal'), bg="white", borderwidth=2)
    password.grid(row=2, column=1, padx=10, pady=10)

    password2_label = Label(frame_contenido, text="REPETIR CONTRASEÑA", font=('calibre', 11, 'bold'), bg="white")
    password2_label.grid(row=3, column=0, padx=30, pady=10, sticky="e")
    password2_pass = Entry(frame_contenido, width=25, show="*", validate="key", textvariable=password2_pass_var,validatecommand=(validate_cmd, '%P'), font=('calibre', 17, 'normal'), bg="white",borderwidth=2)
    password2_pass.grid(row=3, column=1, padx=10, pady=10)

    frame_botones = Frame(ventana_registro, bg="white")
    frame_botones.grid(row=4, column=1, padx=10, pady=10)

    boton = Button(frame_botones, text="Guardar", font=('calibre', 10, 'bold'), width=15, bg="#1E78D5", fg="white",activebackground="#1E78D5", activeforeground="white", command=boton_guardar)
    boton.grid(row=0, column=0, padx=10, pady=20)

    boton2 = Button(frame_botones, text="Cancelar", font=('calibre', 10, 'bold'), width=15, bg="#1E78D5", fg="white",activebackground="#1E78D5", activeforeground="white",command=return_to_main_from_signup)
    boton2.grid(row=0, column=1, padx=10, pady=20)




def User_interface():
    # vamos a ocultar la ventana principal
    login_window.withdraw()

    # crear nueva ventana para el Login
    User_interface = Toplevel(login_window)
    User_interface.title("User_interface")
    User_interface.geometry("400x450")
    User_interface.config(bg="white")

# crear ventana principal de la interfaz
global root
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
                    font=('calibre', 9, 'bold'),
                    cursor="hand2",
                    justify="center",
                    activebackground="#1E78D5",
                    activeforeground="white",
                    bg="#007dfe",
                    fg="white",
                    highlightthickness = 0,
                    padx=10,
                    pady=5).pack(padx=20, pady=20)

# Creando un botón en la interfaz con el nombre 'Sign up'
boton_Sign_up = Button(root,
                    text="Sign up",
                    command=Sign_up,
                    width=10,
                    height=2,
                    font=('calibre', 9, 'bold'),
                    cursor="hand2",
                    justify="center",
                    activebackground="#1E78D5",
                    activeforeground="white",
                    bg="#007dfe",
                    fg="white",
                    highlightthickness=0,
                    padx=10,
                    pady=5).pack(padx=20, pady=20)

root.mainloop()
