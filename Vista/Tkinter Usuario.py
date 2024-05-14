import tkinter as tk
import pymysql
from tkinter import messagebox
import Modelo.CRUDUsuario
from Presentador import Usuarios
from MainIngresoVirus import VentanaVirus
from VistaADN import VentanaADNS
from MainEliminacionSintomas import VentanaEliminacionSintomas
import MainIngresoADN
import VistaBanco

def salir_del_usuario_actual(ventana_actual):
    # Mostrar la ventana principal
    ventana.deiconify()

    # Cerrar la ventana actual
    ventana_actual.destroy()

def abrir_ventana_banco():
    vista_banco = VistaBanco.VistaBanco()
    vista_banco.run()
def abrir_ventana_secundaria(ventana_actual):
    # Ocultar la ventana actual
    ventana_actual.withdraw()

    # Crear y mostrar la ventana secundaria
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Ventana Secundaria")
    ventana_secundaria.minsize(width=400, height=200)
    ventana_secundaria.config(padx=30, pady=30)


    # Botón para ingresar a la ventana Eliminacion sintomas
    tk.Button(ventana_secundaria, text="Agregación/Eliminación sintomas", command=lambda: eliminacion_sintomas(ventana_secundaria)).pack(pady=10)

    # Botón para ingresar a la ventana ingreso virus
    tk.Button(ventana_secundaria, text="ingresar virus", command=lambda: ingresar_virus(ventana_secundaria)).pack(pady=10)

    # Botón para ingresar a la ventana ingreso ADN

    tk.Button(ventana_secundaria, text="Banco de Muestra", command=abrir_ventana_banco).pack(pady=10)

    tk.Button(ventana_secundaria, text="ingresar Secuencia de ADN", command=lambda: ingresar_SecADN(ventana_secundaria)).pack(pady=10)

    # Botón para salir del usuario actual
    tk.Button(ventana_secundaria, text="Salir del Usuario",command=lambda: salir_del_usuario_actual(ventana_secundaria)).pack(pady=10)




def volver_a_principal(ventana_actual):
    # Mostrar la ventana principal
    ventana.deiconify()

    # Cerrar la ventana actual
    ventana_actual.destroy()

def eliminacion_sintomas(ventana_secundaria):
    # Ocultar la ventana actual
    ventana_secundaria.withdraw()

    VentanaEliminacion = tk.Toplevel(ventana)
    VentanaEliminacion.title("Eliminación de síntomas")
    VentanaEliminacion.geometry("600x500")

    app_sintomas2 = VentanaEliminacionSintomas(VentanaEliminacion)

def ingresar_SecADN(ventana_secundaria):
    # Ocultar la ventana actual
    ventana_secundaria.withdraw()

    ventana_SecADN = tk.Toplevel(ventana)
    ventana_SecADN.title("Ingreso ADN")
    ventana_SecADN.geometry("600x500")

    app_sintomas = VentanaADNS(ventana_SecADN)

def ingresar_virus(ventana_secundaria):
    # Ocultar la ventana actual
    ventana_secundaria.withdraw()

    ventana_virus = tk.Toplevel(ventana)
    ventana_virus.title("Ingreso de datos de virus")
    ventana_virus.geometry("600x500")

    app_virus = VentanaVirus(ventana_virus)


def open_login_window():
    def verificar_credenciales():
        nombre_usuario_ingresado = cuadro_usuario.get()
        contraseña_ingresada = cuadro_contraseña.get()

        # Conectar a la base de datos MySQL
        conexion = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='proyecto_agil'
        )
        cursor = conexion.cursor()

        # Realizar una consulta para obtener los usuarios con las credenciales ingresadas
        cursor.execute("SELECT * FROM usuarios WHERE nombreUsuario = %s AND contraseña = %s",
                       (nombre_usuario_ingresado, contraseña_ingresada))
        usuarios = cursor.fetchall()

        # Cerrar la conexión a la base de datos
        conexion.close()

        # si se encontró al menos un usuario con las credenciales proporcionadas se realizara el if
        # de lo contrario, la variable usuarios estara vacia y se realizara el else
        if usuarios:
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
            abrir_ventana_secundaria(login_window)  # llevara a una ventana secundaria al ingersar correctamente
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    # Ocultar la ventana principal
    ventana.withdraw()

    login_window = tk.Toplevel(ventana)
    login_window.title("Log In")
    login_window.minsize(width=400, height=200)
    login_window.config(padx=30, pady=30)

    # Contenedor para alinear elementos
    frame = tk.Frame(login_window)
    frame.pack(pady=10)

    # Campos de entrada para nombre de usuario y contraseña
    tk.Label(frame, text="Nombre de Usuario:").grid(row=0, column=0, pady=5, padx=5, sticky="w")
    cuadro_usuario = tk.Entry(frame)
    cuadro_usuario.grid(row=0, column=1, pady=5, padx=5)

    tk.Label(frame, text="Contraseña:").grid(row=1, column=0, pady=5, padx=5, sticky="w")
    cuadro_contraseña = tk.Entry(frame, show="*")
    cuadro_contraseña.grid(row=1, column=1, pady=5, padx=5)

    # Botón de inicio de sesión
    tk.Button(login_window, text="Iniciar Sesión", command=verificar_credenciales).pack(pady=10)

    # Botón para volver a la ventana principal y cerrar la ventana de registro
    tk.Button(login_window, text="Volver a Principal", command=lambda: volver_a_principal(login_window)).pack(pady=10)


def ingresar_datos_en_registro():
    global entry_rut, entry_nombre, entry_apellido, entry_nombre_usuario, entry_rol, entry_email, entry_contraseña

    rut = entry_rut.get()
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    nombre_usuario = entry_nombre_usuario.get()
    rol = entry_rol.get()
    email = entry_email.get()
    contraseña = entry_contraseña.get()

    # Mapear roles a valores numéricos (ajusta según tus necesidades)
    roles = {"Médico": 1, "Programador": 2, "Investigador": 3, "Infectólogo": 4, "Autoridad": 5}
    rol_numeric = roles.get(rol)

    # Crear un objeto de tipo Usuario
    usuario = Usuarios.Usuarios(nombre, apellido, nombre_usuario, rut, rol, email, contraseña)

    # Solicitar al CRUD que realice la inserción (ajusta esto según tu implementación real)
    Modelo.CRUDUsuario.ingresar(usuario)

    messagebox.showinfo("Éxito", "Datos de usuario ingresados correctamente")

def open_signup_window():
    global entry_rut, entry_nombre, entry_apellido, entry_nombre_usuario, entry_rol, entry_email, entry_contraseña

    # Ocultar la ventana principal
    ventana.withdraw()

    signup_window = tk.Toplevel(ventana)
    signup_window.title("Sign Up")
    signup_window.minsize(width=400, height=200)
    signup_window.config(padx=30, pady=30)

    # Contenedor para alinear elementos
    frame = tk.Frame(signup_window)
    frame.pack(pady=10)

    # Campos de entrada para los datos del usuario
    tk.Label(frame, text="RUT:").grid(row=0, column=0, pady=5, padx=5, sticky="w")
    entry_rut = tk.Entry(frame)
    entry_rut.grid(row=0, column=1, pady=5, padx=5)

    tk.Label(frame, text="Nombre:").grid(row=1, column=0, pady=5, padx=5, sticky="w")
    entry_nombre = tk.Entry(frame)
    entry_nombre.grid(row=1, column=1, pady=5, padx=5)

    tk.Label(frame, text="Apellido:").grid(row=2, column=0, pady=5, padx=5, sticky="w")
    entry_apellido = tk.Entry(frame)
    entry_apellido.grid(row=2, column=1, pady=5, padx=5)

    tk.Label(frame, text="Nombre de Usuario:").grid(row=3, column=0, pady=5, padx=5, sticky="w")
    entry_nombre_usuario = tk.Entry(frame)
    entry_nombre_usuario.grid(row=3, column=1, pady=5, padx=5)

    # crear una lista desplegable con opciones
    tk.Label(frame, text="Rol:").grid(row=4, column=0, pady=5, padx=5, sticky="w")
    roles = ["Médico", "Programador", "Investigador", "Infectólogo", "Autoridad"]
    entry_rol = tk.StringVar(frame)
    entry_rol.set(roles[0])  # Valor predeterminado
    tk.OptionMenu(frame, entry_rol, *roles).grid(row=4, column=1, pady=5, padx=5)

    tk.Label(frame, text="Email:").grid(row=5, column=0, pady=5, padx=5, sticky="w")
    entry_email = tk.Entry(frame)
    entry_email.grid(row=5, column=1, pady=5, padx=5)

    tk.Label(frame, text="Contraseña:").grid(row=6, column=0, pady=5, padx=5, sticky="w")
    entry_contraseña = tk.Entry(frame, show="*")
    entry_contraseña.grid(row=6, column=1, pady=5, padx=5)

    # Botón para ingresar los datos del usuario
    tk.Button(signup_window, text="Ingresar Datos", command=ingresar_datos_en_registro).pack(pady=10)

    # Botón para volver a la ventana principal y cerrar la ventana de registro
    tk.Button(signup_window, text="Volver a Principal", command=lambda: volver_a_principal(signup_window)).pack(pady=10)
def abrir_ventana_adn(ventana_secundaria):
    # Ocultar la ventana actual
    ventana_secundaria.withdraw()

    # Crear y mostrar la ventana de MainIngresoADN
    ventana_adn = tk.Toplevel(ventana)
    ventana_adn.title("Ingreso de ADN")
    ventana_adn.geometry("600x500")

    # Crear una instancia de la clase VentanaADN
    app_adn = MainIngresoADN.VentanaADN(ventana_adn, ventana_secundaria)
    app_adn.abrir_desde_otra_ventana()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("menu principal")
ventana.minsize(width=400, height=200)
ventana.config(padx=30, pady=30)

# Botón "Log In"
login_button = tk.Button(ventana, text="Log In", command=open_login_window)
login_button.pack(pady=10)

# Botón "Sign Up"
signup_button = tk.Button(ventana, text="Sign Up", command=open_signup_window)
signup_button.pack(pady=10)

# Inicia el bucle principal de la aplicación
ventana.mainloop()

