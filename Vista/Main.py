#import tkinter as tk
import re
from tkinter import *
from tkinter import messagebox
from tkinter import Canvas
from PIL import ImageTk, Image
import random
import string
import time
import pymysql
import os
from DTO.Varios import hash_md5
from dotenv import load_dotenv
from email.message import EmailMessage
import smtplib
import ssl

load_dotenv()


def menu_usuario():
    login_window.withdraw()
    global Menu_usu
    Menu_usu = Toplevel()
    Menu_usu.title("MENU DE USUARIO")
    Menu_usu.minsize(width=400, height=400)
    Menu_usu.config(bg="white" ,padx=30, pady=30)

    Frame_up = Frame(Menu_usu, width=400, height=50, bg="white")
    Frame_up.grid(row=0, column=1)

    Frame_down = Frame(Menu_usu, width=400, height=380, bg="white")
    Frame_down.grid(row=1, column=1)

    image_path = image_path = os.path.join(os.path.dirname(__file__), '..', 'img',
                                           'PNK.jpeg')  # Replace with your image path
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    # Step 4: Create a Canvas widget and add the image to it
    canvas = Canvas(Frame_down, width=200, height=200)
    canvas.pack()

    # Add the image to the canvas
    canvas.create_image(0, 0, anchor=NW, image=photo)

    # Keep a reference to avoid garbage collection
    canvas.image = photo

    Header = Label(Frame_up, text="PNK", font=('Poppins', 23, "bold"), bg="white").place(x=160, y=5)
    return_btn = Button(Menu_usu,
                        text='Cerrar sesion',
                        font=('calibre', 10, 'bold'),
                        width=10,
                        bg="#007dfe",
                        fg="white",
                        activebackground="#1E78D5",
                        activeforeground="white",
                        command=return_to_main_from_menu_usu).place(x=145, y=280)

global login_window
global Email_var
def Login():# Esta función se ejecutará cuando se presione el botón
    def cambiar_contra():

        ventana_forgot.withdraw()
        global ventana_contra
        ventana_contra = Toplevel(root)
        ventana_contra.title("RECUPERACION DE CONTRASEÑA")
        ventana_contra.geometry("370x350")
        ventana_contra.configure(bg="white")

        def validar_contra(contraseña):
            if len(contraseña) < 8 or len(contraseña) > 24:
                return False
            if not re.search(r'[A-Z]', contraseña):
                return False
            if not re.search(r'[0-9]', contraseña):
                return False
            if not re.search(r'[\W_]', contraseña):  # \W busca cualquier carácter no alfanumérico
                return False
            return True

        def validar_contraseña():
            password1 = passw_var.get()
            password2 = re_passw_var.get()

            if password1 != password2:
                messagebox.showwarning("Advertencia", "Las contraseñas no coinciden")
                return False
            if not validar_contra(password1):
                messagebox.showwarning("Advertencia",
                                       "La contraseña debe tener Mayúsculas, números y caracteres especiales")
                return False
            return True

        def change_password():
            Email = Email_var.get()
            password = hash_md5(passw_var.get())
            re_password = hash_md5(re_passw_var.get())

            if validar_contraseña():
                conexion = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='',
                    db='login_interface'
                )
                sql_login = conexion.cursor()

                sql_login.execute("UPDATE `usuario` SET `password` = %s WHERE `usuario`.`email` = %s;",
                                  (password, Email))

                conexion.close()
                messagebox.showinfo("YAY!", "contraseña Cambiada correctamente")
                from_recuperarContra_to_login()




        passw_var = StringVar()
        re_passw_var = StringVar()
        def submit_password():
            Email = Email_var.get()
            password = passw_var.get()
            re_password = re_passw_var.get()
            if len(password) == 0:
                messagebox.showerror("ADVERTENCIA", "Debe completar el campo: Email")
            elif len(re_password) == 0:
                messagebox.showerror("ADVERTENCIA", "Debe completar el campo: Contraseña")
            else:
                Email = Email_var.get()
                password = passw_var.get()
                re_password = re_passw_var.get()
                print(Email)
                print(password)
                print(re_password)
                change_password()

        Frame_up = Frame(ventana_contra, width=400, height=70, bg="white")
        Frame_up.grid(row=0, column=1)

        Frame_down = Frame(ventana_contra, width=400, height=380, bg="white")
        Frame_down.grid(row=1, column=1)

        Header = Label(Frame_up, text="CAMBIO CONTRASEÑA", font=('Poppins', 18, "bold"), bg="white").place(x=40, y=20)

        line = Label(Frame_up, width=40, text="", height=1, bg="#007dfe", anchor=NW)
        line.place(x=35, y=65)

        Email_label = Label(Frame_down, text='Contraseña', font=('calibre', 11, 'bold'), bg="white").place(x=70, y=45)

        Email_entry = Entry(Frame_down,
                            textvariable=passw_var,
                            font=('calibre', 17, 'normal'),
                            show='*',
                            bg="white",
                            borderwidth=2,
                            width=20).place(x=55, y=70)
        # if name_entry=='':

        #   creating a label for password
        passw_label = Label(Frame_down, text='Repetir Contraseña', font=('calibre', 11, 'bold'), bg="white").place(x=65, y=118)

        # creating an entry for password
        passw_entry = Entry(Frame_down,
                            textvariable=re_passw_var,
                            font=('calibre', 17, 'normal'),
                            show='*',
                            borderwidth=2,
                            bg="white",
                            width=20).place(x=55, y=145)

        # creating a button using the widget
        # Button that will call the submit function
        sub_btn = Button(Frame_down,
                         text='Enviar',
                         font=('calibre', 10, 'bold'),
                         width=15,
                         bg="#007dfe",
                         fg="white",
                         activebackground="#1E78D5",
                         activeforeground="white",
                         command=submit_password).place(x=125, y=195)


    def verificar_credenciales():
        Email_usu = Email_var.get()
        password_usu = hash_md5(passw_var.get())

        conexion = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='login_interface'
        )
        sql_login = conexion.cursor()

        sql_login.execute("SELECT email, password FROM usuario WHERE email = %s AND password = %s AND estado = 1",
                       (Email_usu, password_usu))

        usuario = sql_login.fetchone()

        conexion.close()

        if usuario:
            messagebox.showinfo("ÉXITO", "Inicio de sesión exitoso")
            menu_usuario()
        else:
            messagebox.showerror("ERROR", "Usuario o contraseña incorrectos\nó usuario desactivado")

    # vamos a ocultar la ventana principal
    root.withdraw()


    global login_window
    # crear nueva ventana para el Login
    login_window = Toplevel(root)
    login_window.title("INICIO DE SESIÓN")
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


    global Email_var
    Email_var = StringVar()
    passw_var = StringVar()
    def Help_function():
        print("Help")

    def submit():

        Email = Email_var.get()
        password = passw_var.get()
        if len(Email) == 0:
            messagebox.showinfo("ADVERTENCIA", "llenar el campo: correo")
        elif len(password) == 0:
            messagebox.showinfo("ADVERTENCIA", "llenar el campo: contraseña")
        else:
            Email = Email_var.get()
            password = hash_md5(passw_var.get())
            print(Email)
            print(password)
            verificar_credenciales()

    def Forgot_password():
        login_window.withdraw()
        global ventana_forgot
        ventana_forgot = Toplevel(root)
        ventana_forgot.title("RECUPERACION DE CONTRASEÑA")
        ventana_forgot.geometry("650x450")
        ventana_forgot.configure(bg="white")

        def validate_length(new_value):
            max_length = 25
            if len(new_value) > max_length:
                return False
            return True

        def generar_codigo_aleatorio(longitud):
            caracteres = string.ascii_letters + string.digits
            return ''.join(random.choice(caracteres) for _ in range(longitud))

        def display_message(message):
            message_label.config(text=message)

        def save_code_to_database(codigo_aleatorio):
            Email_usu = Email_var.get()

            conexion = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='login_interface'
            )
            sql_login = conexion.cursor()

            sql_login.execute("UPDATE `usuario` SET `codigo_temporal` = %s WHERE `usuario`.`email` = %s;",
                              (codigo_aleatorio, Email_usu))

            conexion.close()

        def boton_codigo():
            global codigo_aleatorio
            codigo_aleatorio = generar_codigo_aleatorio(6)
            print(codigo_aleatorio)
            save_code_to_database(codigo_aleatorio)
            display_message("Código de Recuperación Enviado\nse actualizará en cinco minutos")
            # Change the code every 5 minutes
            ventana_forgot.after(300000, boton_codigo)
            email_sender = "correodepruebas716@gmail.com"
            email_receiver = correo.get()  # Assuming 'correo' is the Entry field for the email address
            subject = "CÓDIGO DE RECUPERACIÓN"
            body = f"Su código de recuperación es: {codigo_aleatorio}"

            em = EmailMessage()
            em["From"] = email_sender
            em["To"] = email_receiver
            em["Subject"] = subject
            em.set_content(body)

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(email_sender, "v a h b i o b v i z k n y l o g")  # Replace with your email password
                smtp.send_message(em)

            # Show a messagebox informing the user
            messagebox.showinfo("CÓDIGO DE RECUPERACIÓN","Código de Recuperación enviado. Verifique su correo electrónico.")

        global codigo_aleatorio
        def verify_same_code():
            codigo_verificador = codigo.get()
            Email_usu = Email_var.get()

            conexion = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='login_interface'
            )
            sql_login = conexion.cursor()

            sql_login.execute("SELECT codigo_temporal FROM usuario WHERE email = %s ",
                              (Email_usu))
            codigo_temp = sql_login.fetchone()
            conexion.close()
            if codigo_temp:
                codigo_temp = codigo_temp[0]
                # Removing unwanted characters from codigo_temp
                code_without_parentheses = codigo_temp.replace("(", "").replace(")", "").replace(",", "").replace("'", "")
                print("-----------------------------")
                print(Email_usu)
                print(code_without_parentheses)
                print(codigo_verificador)
            else:
                print("error al enviar el codigo temporal a:", Email_usu)

            if codigo_verificador != code_without_parentheses:
                messagebox.showinfo("ERROR", "Codigo verificador no coincide.")
            else:
                ventana_forgot.after_cancel(boton_codigo)
                messagebox.showinfo("EXITO", "Codigo verificador coincide.")
                Email_usu = Email_var.get()

                conexion = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='',
                    db='login_interface'
                )
                sql_login = conexion.cursor()

                sql_login.execute("UPDATE `usuario` SET `estado` = 1 WHERE `usuario`.`email` = %s;",
                                  (Email_usu))

                conexion.close()
                cambiar_contra()


        # Registra la función de validación
        validate_cmd = ventana_forgot.register(validate_length)

        frame_cabecera = Frame(ventana_forgot, bg="white")
        frame_cabecera.grid(row=0, column=1, columnspan=1, padx=10, pady=20)
        cabecera = Label(frame_cabecera, text="RECUPERACION DE CONTRASEÑA", font=('Poppins', 18, "bold"),
                         bg="white", anchor="center")
        cabecera.pack()

        frame_contenido = Frame(ventana_forgot, bg="white")
        frame_contenido.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Etiquetas y campos de entrada dentro del frame de contenido
        correo_label = Label(frame_contenido, text="CORREO", font=('calibre', 11, 'bold'), bg="white")
        correo_label.grid(row=0, column=0, padx=30, pady=10, sticky="e")
        correo = Entry(frame_contenido, width=25, validate="key", validatecommand=(validate_cmd, '%P'),
                       font=('calibre', 17, 'normal'), bg="white", borderwidth=2, state="normal")
        correo.grid(row=0, column=1, padx=10, pady=10)
        correo.insert(0, Email_var.get())  # Insert the value of Email_var into the Entry field
        correo.config(state="disabled")

        boton1 = Button(frame_contenido, text="Enviar Código", font=('calibre', 10, 'bold'), width=15, bg="#1E78D5",
                        fg="white", activebackground="#1E78D5", activeforeground="white", command=boton_codigo)
        boton1.grid(row=1, column=1, padx=1, pady=20)

        codigo_label = Label(frame_contenido, text="INGRESAR CÓDIGO", font=('calibre', 11, 'bold'), bg="white")
        codigo_label.grid(row=2, column=0, padx=30, pady=10, sticky="e")
        codigo = Entry(frame_contenido, width=25, validate="key", validatecommand=(validate_cmd, '%P'),
                       font=('calibre', 17, 'normal'), bg="white", borderwidth=2)
        codigo.grid(row=2, column=1, padx=10, pady=10)

        boton2 = Button(frame_contenido, text="Verificar Código", font=('calibre', 10, 'bold'), width=15,
                        bg="#1E78D5", fg="white", activebackground="#1E78D5", activeforeground="white", command=verify_same_code)
        boton2.grid(row=3, column=1, padx=1, pady=20)

        # Message label to display the code
        message_label = Label(frame_contenido, text="", font=('calibre', 12), bg="white")
        message_label.grid(row=4, column=1, padx=10, pady=10)



    def disable_email():
        Email_usu = Email_var.get()

        conexion = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='login_interface'
        )
        sql_login = conexion.cursor()

        sql_login.execute("SELECT email FROM usuario WHERE email = %s",
                          (Email_usu))

        usuario = sql_login.fetchone()

        conexion.close()

        if usuario:
            conexion = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='login_interface'
            )
            sql_login = conexion.cursor()

            sql_login.execute("UPDATE `usuario` SET `estado` = 0 WHERE `usuario`.`email` = %s;",
                              (Email_usu))

            conexion.close()
            Forgot_password()
        else:
            messagebox.showerror("ERROR", "Ingrese un usuario")


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

    Header = Label(Frame_up, text="INICIO DE SESION", font=('Poppins', 23, "bold"), bg="white").place(x=40, y=20)

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
    passw_label = Label(Frame_down, text='Contraseña', font=('calibre', 11, 'bold'), bg="white").place(x=65, y=118)
    pass_F = Button(Frame_down,
                    text='¿Olvidó su contraseña?',
                    command=disable_email,
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
                    text='Enviar',
                    font=('calibre', 10, 'bold'),
                    width=15,
                    bg="#007dfe",
                    fg="white",
                    activebackground="#1E78D5",
                    activeforeground="white",
                    command=submit).place(x=125, y=195)

    return_btn = Button(Frame_down,
                    text='Regresar',
                    font=('calibre', 10, 'bold'),
                    width=10,
                    bg="#007dfe",
                    fg="white",
                    activebackground="#1E78D5",
                    activeforeground="white",
                    command=return_to_main_from_login).place(x=35, y=320)

    help_btn = Button(Frame_down,
                    text='ayuda',
                    font=('calibre', 10, 'bold'),
                    width=8,
                    bg="#007dfe",
                    fg="white",
                    activebackground="#1E78D5",
                    activeforeground="white",
                    command=cambiar_contra).place(x=305, y=320)


def return_to_main_from_login():
    login_window.withdraw()
    root.deiconify() #restaurar la ventana principal

def return_to_main_from_menu_usu():
    Menu_usu.withdraw()
    root.deiconify() #restaurar la ventana principal

def return_to_main_from_signup():
    ventana_registro.withdraw()
    root.deiconify() #restaurar la ventana principal

def from_recuperarContra_to_main():
    ventana_contra.withdraw()
    root.deiconify()

def from_recuperarContra_to_login():
    ventana_contra.withdraw()
    login_window.deiconify()


def Sign_up():
    root.withdraw()
    global ventana_registro
    ventana_registro = Toplevel(root)
    ventana_registro.title("REGISTRO")
    ventana_registro.geometry("650x450")
    ventana_registro.configure(bg="white")

    def validate_password(password):
        if len(password) < 8 or len(password) > 24:
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[0-9]', password):
            return False
        if not re.search(r'[\W_]', password):  # \W busca cualquier carácter no alfanumérico
            return False
        return True

    def validar_contraseña():
        password1 = password_var.get()
        password2 = password2_var.get()

        if password1 != password2:
            messagebox.showwarning("Advertencia", "Las contraseñas no coinciden")
            return False
        if not validate_password(password1):
            messagebox.showwarning("Advertencia", "La contraseña debe tener Mayusculas, numeros y caracteres")
            return False
        return True

    def validar_correo(email):
        if not email.endswith("@gmail.com"):
            return False
        if len(email) > 45:
            return False
        return True

    usuario_var = StringVar()
    password_var = StringVar()
    correo_var = StringVar()
    password2_var = StringVar()

    def boton_guardar():
        if validar_contraseña():
            usuario = usuario_var.get()
            correo = correo_var.get()
            password = password_var.get()

            if len(usuario) == 0:
                messagebox.showinfo("ADVERTENCIA", "Por favor llenar el campo: usuario")
            elif len(correo) == 0:
                messagebox.showinfo("ADVERTENCIA", "Por favor llenar el campo: correo")
            elif len(password) == 0:
                messagebox.showinfo("ADVERTENCIA", "Por favor llenar el campo: contraseña")
            else:
                password_hash = hash_md5(password)

                if not validar_correo(correo):
                    messagebox.showwarning("Advertencia",
                                           "El correo debe terminar en @gmail.com y tener un máximo de 45 caracteres")
                    return

                try:
                    conexion = pymysql.connect(
                        host='localhost',
                        user='root',
                        password='',
                        db='login_interface'
                    )
                    sql_signup = conexion.cursor()
                    sql_signup.execute(
                        "INSERT INTO usuario (nombre_completo, email, password, estado) VALUES (%s, %s, %s, 1)",
                        (usuario, correo, password_hash)
                    )
                    conexion.commit()
                    conexion.close()
                    messagebox.showinfo("ÉXITO", "Datos de usuario ingresados correctamente")
                    Login()
                    ventana_registro.withdraw()
                except pymysql.MySQLError as e:
                    messagebox.showerror("ERROR", f"Error en la base de datos: {str(e)}")

    frame_cabecera = Frame(ventana_registro, bg="white")
    frame_cabecera.grid(row=0, column=1, columnspan=1, padx=10, pady=10)
    cabecera = Label(frame_cabecera, text="Introduzca los datos solicitados", font=('Poppins', 18, "bold"), bg="white", anchor="center")
    cabecera.pack()

    frame_contenido = Frame(ventana_registro, bg="white")
    frame_contenido.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Etiquetas y campos de entrada dentro del frame de contenido
    usuario_label = Label(frame_contenido, text="USUARIO", font=('calibre', 11, 'bold'), bg="white")
    usuario_label.grid(row=0, column=0, padx=30, pady=10, sticky="e")
    usuario = Entry(frame_contenido, width=25, textvariable=usuario_var, font=('calibre', 17, 'normal'), bg="white", borderwidth=2)
    usuario.grid(row=0, column=1, padx=10, pady=10)

    correo_label = Label(frame_contenido, text="CORREO", font=('calibre', 11, 'bold'), bg="white")
    correo_label.grid(row=1, column=0, padx=30, pady=10, sticky="e")
    correo = Entry(frame_contenido, width=25, textvariable=correo_var, font=('calibre', 17, 'normal'), bg="white", borderwidth=2)
    correo.grid(row=1, column=1, padx=10, pady=10)

    password_label = Label(frame_contenido, text="CONTRASEÑA", font=('calibre', 11, 'bold'), bg="white")
    password_label.grid(row=2, column=0, padx=30, pady=10, sticky="e")
    password = Entry(frame_contenido, width=25, show="*", textvariable=password_var, font=('calibre', 17, 'normal'), bg="white", borderwidth=2)
    password.grid(row=2, column=1, padx=10, pady=10)

    password2_label = Label(frame_contenido, text="REPETIR CONTRASEÑA", font=('calibre', 11, 'bold'), bg="white")
    password2_label.grid(row=3, column=0, padx=30, pady=10, sticky="e")
    password2 = Entry(frame_contenido, width=25, show="*", textvariable=password2_var, font=('calibre', 17, 'normal'), bg="white", borderwidth=2)
    password2.grid(row=3, column=1, padx=10, pady=10)

    frame_botones = Frame(ventana_registro, bg="white")
    frame_botones.grid(row=4, column=1, padx=10, pady=10)

    boton = Button(frame_botones, text="Guardar", font=('calibre', 10, 'bold'), width=15, bg="#1E78D5", fg="white", activebackground="#1E78D5", activeforeground="white", command=boton_guardar)
    boton.grid(row=0, column=0, padx=10, pady=20)

    boton2 = Button(frame_botones, text="Cancelar", font=('calibre', 10, 'bold'), width=15, bg="#1E78D5", fg="white", activebackground="#1E78D5", activeforeground="white", command=return_to_main_from_signup)
    boton2.grid(row=0, column=1, padx=10, pady=20)




def User_interface():
    # vamos a ocultar la ventana principal
    login_window.withdraw()

    # crear nueva ventana para el Login
    User_interface = Toplevel(login_window)
    User_interface.title("INTERFAZ DE USUARIO")
    User_interface.geometry("400x450")
    User_interface.config(bg="white")

# crear ventana principal de la interfaz
global root
root = Tk()
# agegarle un nombre a la ventana
root.title("Menu principal")
# ajustar el tamaño de la ventana
root.minsize(width=300, height=250)
# agregar relleno a los lados de la ventana principal
root.config(padx=30, pady=30)

# Colocar un botón en la interfaz con el nombre 'Login'
boton_Login = Button(root,
                    text="Inicio de sesión",
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
                    text="Registro",
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
