
#importar tkinter como tk
import tkinter as tk


# crear una funcion que,al presionar el boton, se realice lo que esta dentro de esta
# las funciones deben ser creadas antes que el boton que las utilizara
# de lo contrario, no funcionara el proceso
def ingresar_datos():
    # Esta función se ejecutará cuando se presione el botón

    # vamos a ocultar la ventana principal
    ventana.withdraw()

    # crear nueva ventana para hacer_algo
    login_window = tk.Toplevel(ventana)
    login_window.title("Log In")

    # Contenedor para alinear elementos, nos permitira poner los rextos a la izquierda
    # aun no estoy seguro de como funciona
    frame = tk.Frame(login_window)
    frame.pack(pady=10)

    # creacion de un campo para ingresar un rut
    tk.Label(frame, text="RUT:").grid(row=0, column=0, pady=5, padx=5, sticky="w")
    entry_rut = tk.Entry(frame)
    entry_rut.grid(row=0, column=1, pady=5, padx=5)

# crear ventana principal de la interfaz
ventana = tk.Tk()
# agegarle un nombre a la ventana
ventana.title("menu principal")
# ajustar el tamaño de la ventana
ventana.minsize(width=400, height=200)
# agregar relleno a los lados de la ventana principal
ventana.config(padx=30, pady=30)


# Colocar un botón en la interfaz con el nombre 'click me'
# que realizara el contenido de la funcion anteriormente creada 'hacer_algo'
boton_ingresar_datos = tk.Button(ventana, text="click me", command=ingresar_datos)
# agregar el boton a la ventana principal
boton_ingresar_datos.pack(pady=10)

# ejecutar el bucle principal
# Esto mantiene la ventana abierta y espera a que el usuario realice acciones
ventana.mainloop()