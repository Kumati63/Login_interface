import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

class VentanaADN:

    def abrir_desde_otra_ventana(self):
        if self.ventana_usuario:
            self.ventana_usuario.deiconify()  # Mostrar la ventana principal de la aplicación
            self.ventana_usuario.lift()

    def __init__(self, master, ventana_usuario):
        self.master = master
        self.master.title("Ingreso de ADN")
        self.master.geometry("600x500")
        self.ventana_usuario = ventana_usuario  # Agregamos referencia a la ventana principal

        self.Secuencia_ADN = tk.StringVar()
        self.NombreADN = tk.StringVar()
        self.crear_interfaz()
        self.ventana_usuario = ventana_usuario
        self.crear_interfaz()


    def crear_interfaz(self):
        self.marco = tk.LabelFrame(self.master, text="Ventana de ingreso de ADN")
        self.marco.place(x=50, y=50, width=500, height=400)

        lblNombreCien = tk.Label(self.marco, text="Secuencia de adn").grid(column=0, row=0, padx=5, pady=5)
        lblNombreCien = tk.Entry(self.marco, textvariable=self.Secuencia_ADN)
        lblNombreCien.grid(column=1, row=0)

        lblNombre = tk.Label(self.marco, text="Nombre de ADN").grid(column=0, row=1, padx=5, pady=5)
        lblNombre = tk.Entry(self.marco, textvariable=self.NombreADN)
        lblNombre.grid(column=1, row=1)

        tk.Label(self.marco, text="DATOS DE SECUENCIA DE ADN INGRESADOS", fg="black").grid(column=0, row=3, columnspan=4)

        self.vistadatos = ttk.Treeview(self.marco)
        self.vistadatos.grid(column=0, row=4, columnspan=4)
        self.vistadatos["columns"] = ("Secuencia_ADN", "NombreADN")
        self.vistadatos.column("#0", width=0, stretch=tk.NO)
        self.vistadatos.column("Secuencia_ADN", width=250, anchor=tk.CENTER)
        self.vistadatos.column("NombreADN", width=240, anchor=tk.CENTER)
        self.vistadatos.heading("Secuencia_ADN", text="Secuencia_ADN", anchor=tk.CENTER)
        self.vistadatos.heading("NombreADN", text="NombreADN", anchor=tk.CENTER)

        btnGuardar = tk.Button(self.marco, text="Guardar", command=self.guardar)
        btnGuardar.grid(column=0, row=5)

        btnEliminar = tk.Button(self.marco, text="Eliminar", command=self.eliminar)
        btnEliminar.grid(column=2, row=5)

        self.mostrar_datos()

    def guardar(self):
        secuencia = self.Secuencia_ADN.get()
        nombreadn = self.NombreADN.get()

        if secuencia and nombreadn:
            try:
                conexion = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='',
                    db='proyecto_agil'
                )
                cursor = conexion.cursor()

                query = "INSERT INTO adn (Secuencia_ADN,NombreADN) VALUES (%s, %s)"
                cursor.execute(query, (secuencia, nombreadn))
                conexion.commit()

                messagebox.showinfo("Éxito", "Datos guardados correctamente")

                self.mostrar_datos()

            except pymysql.Error as e:
                messagebox.showerror("Error", f"Error al guardar datos en la base de datos: {e}")

            finally:
                if conexion:
                    conexion.close()
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def eliminar(self):
        secuencia = self.Secuencia_ADN.get()
        nombreadn = self.NombreADN.get()

        if secuencia and nombreadn:
            try:
                conexion = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='',
                    db='proyecto_agil'
                )
                cursor = conexion.cursor()

                query = "DELETE FROM adn WHERE Secuencia_ADN = %s AND NombreADN = %s"
                cursor.execute(query, (secuencia, nombreadn))
                conexion.commit()

                messagebox.showinfo("Éxito", "Datos eliminados correctamente")

                self.mostrar_datos()

            except pymysql.Error as e:
                messagebox.showerror("Error", f"Error al eliminar datos de la base de datos: {e}")

            finally:
                if conexion:
                    conexion.close()
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def mostrar_datos(self):
        try:
            conexion = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='proyecto_agil'
            )
            cursor = conexion.cursor()

            query = "SELECT Secuencia_ADN, NombreADN FROM adn"
            cursor.execute(query)
            datos = cursor.fetchall()

            # Limpiamos los datos existentes en el Treeview
            for record in self.vistadatos.get_children():
                self.vistadatos.delete(record)

            # Insertamos los nuevos datos en el Treeview
            for dato in datos:
                self.vistadatos.insert("", "end", values=dato)

        except pymysql.Error as e:
            messagebox.showerror("Error", f"Error al obtener datos de la base de datos: {e}")

        finally:
            if conexion:
                conexion.close()

if __name__ == "__main__":
    root = tk.Tk()
    ventana_usuario = None  # Cambiar esto si tienes una referencia real a la ventana principal
    app = VentanaADN(root, ventana_usuario)
    root.mainloop()
