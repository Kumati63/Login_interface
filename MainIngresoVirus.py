import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

class VentanaVirus:
    def __init__(self, master):
        self.master = master
        self.master.title("Ingreso de datos de virus")
        self.master.geometry("600x500")

        self.nombreCientifico = tk.StringVar()
        self.nombre= tk.StringVar()
        self.fechaDescubrimiento= tk.StringVar()

        self.crear_interfaz()

    def crear_interfaz(self):
        self.marco = tk.LabelFrame(self.master, text="Ventana de ingreso de datos")
        self.marco.place(x=50, y=50, width=500, height=400)

        lblNombreCien = tk.Label(self.marco, text="Nombre Cientifico").grid(column=0, row=0, padx=5, pady=5)
        lblNombreCien = tk.Entry(self.marco, textvariable=self.nombreCientifico)
        lblNombreCien.grid(column=1, row=0)

        lblNombre = tk.Label(self.marco, text="Nombre").grid(column=0, row=1, padx=5, pady=5)
        lblNombre = tk.Entry(self.marco, textvariable=self.nombre)
        lblNombre.grid(column=1, row=1)

        lblFechaDes = tk.Label(self.marco, text="Fecha de descubrimiento").grid(column=0, row=2, padx=5, pady=5)
        lblFechaDes = tk.Entry(self.marco, textvariable=self.fechaDescubrimiento)
        lblFechaDes.grid(column=1, row=2)

        tk.Label(self.marco, text="DATOS INGRESADOS", fg="green").grid(column=0, row=3, columnspan=4)

        self.vistadatos = ttk.Treeview(self.marco)
        self.vistadatos.grid(column=0, row=4, columnspan=4)
        self.vistadatos["columns"] = ("nombreCientifico", "nombre","fechaDescubrimiento")
        self.vistadatos.column("#0", width=0, stretch=tk.NO)
        self.vistadatos.column("nombreCientifico", width=170, anchor=tk.CENTER)
        self.vistadatos.column("nombre", width=160, anchor=tk.CENTER)
        self.vistadatos.column("fechaDescubrimiento", width=160, anchor=tk.CENTER)
        self.vistadatos.heading("nombreCientifico", text="nombreCientifico", anchor=tk.CENTER)
        self.vistadatos.heading("nombre", text="nombre", anchor=tk.CENTER)
        self.vistadatos.heading("fechaDescubrimiento", text="fechaDescubrimiento", anchor=tk.CENTER)

        btnGuardar = tk.Button(self.marco, text="Guardar", command=self.guardar)
        btnGuardar.grid(column=1, row=5)

        self.mostrar_datos()

    def guardar(self):
        nombreCien = self.nombreCientifico.get()
        nombre_virus = self.nombre.get()
        fecha_desc = self.fechaDescubrimiento.get()

        if nombreCien and nombre_virus and fecha_desc:
            try:
                conexion = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='',
                    db='proyecto_agil'
                )
                cursor = conexion.cursor()

                query = "INSERT INTO Virus (nombreCientifico, nombre, fechaDesc) VALUES (%s, %s, %s)"
                cursor.execute(query, (nombreCien, nombre_virus,fecha_desc))
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

    def mostrar_datos(self):
        self.vistadatos.delete(*self.vistadatos.get_children())

        try:
            conexion = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='proyecto_agil'
            )
            cursor = conexion.cursor()

            query = "SELECT nombreCientifico, nombre, fechaDesc FROM Virus"
            cursor.execute(query)
            datos = cursor.fetchall()

            for dato in datos:
                self.vistadatos.insert("", "end", values=dato)

        except pymysql.Error as e:
            messagebox.showerror("Error", f"Error al obtener datos de la base de datos: {e}")

        finally:
            if conexion:
                conexion.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaVirus(root)
    root.mainloop()
