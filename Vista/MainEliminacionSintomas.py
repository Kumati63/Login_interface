import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

class VentanaEliminacionSintomas:
    def __init__(self, master):
        self.master = master
        self.master.title("Agregación/Eliminacion de sintomas")
        self.master.geometry("600x500")

        self.nombre = tk.StringVar()
        self.sintoma = tk.StringVar()

        self.crear_interfaz()

    def obtener_nombres_virus_desde_bd(self):
        try:
            conexion = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='proyecto_agil'
            )
            cursor = conexion.cursor()

            query = "SELECT nombreCientifico FROM Virus"
            cursor.execute(query)
            nombres_virus = [row[0] for row in cursor.fetchall()]

            return nombres_virus

        except pymysql.Error as e:
            messagebox.showerror("Error", f"Error al obtener nombres de virus: {e}")

        finally:
            if conexion:
                conexion.close()

    def obtener_sintomas_desde_bd(self):
        try:
            conexion = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='proyecto_agil'
            )
            cursor = conexion.cursor()

            query = "SELECT DISTINCT sintoma FROM Sintomas"
            cursor.execute(query)
            sintomas = [row[0] for row in cursor.fetchall()]

            return sintomas

        except pymysql.Error as e:
            messagebox.showerror("Error", f"Error al obtener síntomas de la base de datos: {e}")

        finally:
            if conexion:
                conexion.close()

    def crear_interfaz(self):
        self.marco = tk.LabelFrame(self.master, text="Ventana de eliminacion de sintomas")
        self.marco.place(x=50, y=50, width=500, height=400)

        # Obtener nombres de virus desde la base de datos
        nombres_virus = self.obtener_nombres_virus_desde_bd()

        lblNombre = tk.Label(self.marco, text="Nombre de virus").grid(column=0, row=0, padx=5, pady=5)
        self.lista_virus = ttk.Combobox(self.marco, values=nombres_virus, textvariable=self.nombre)
        self.lista_virus.grid(column=1, row=0)

        lblSintoma = tk.Label(self.marco, text="Síntoma").grid(column=0, row=1, padx=5, pady=5)
        self.lista_sintomas = ttk.Combobox(self.marco, values=self.obtener_sintomas_desde_bd(), textvariable=self.sintoma)
        self.lista_sintomas.grid(column=1, row=1)

        tk.Label(self.marco, text="o ingrese un nuevo síntoma:").grid(column=0, row=2, pady=5)
        self.entry_sintoma = tk.Entry(self.marco, textvariable=self.sintoma)
        self.entry_sintoma.grid(column=1, row=2, pady=5)

        tk.Label(self.marco, text="DATOS INGRESADOS", fg="green").grid(column=0, row=3, columnspan=4)

        self.vistadatos = ttk.Treeview(self.marco)
        self.vistadatos.grid(column=0, row=4, columnspan=4)
        self.vistadatos["columns"] = ("nombre ","sintoma")
        self.vistadatos.column("#0", width=0, stretch=tk.NO)
        self.vistadatos.column("nombre ", width=250, anchor=tk.CENTER)
        self.vistadatos.column("sintoma", width=245, anchor=tk.CENTER)
        self.vistadatos.heading("nombre ", text="Nombre ", anchor=tk.CENTER)
        self.vistadatos.heading("sintoma", text="Síntoma", anchor=tk.CENTER)

        btnGuardar = tk.Button(self.marco, text="Guardar", command=self.guardar)
        btnGuardar.grid(column=0, row=5)

        btnEliminar = tk.Button(self.marco, text="Eliminar", command=self.eliminar)
        btnEliminar.grid(column=2, row=5)

        self.mostrar_datos()

    def guardar(self):
        nombre_virus = self.nombre.get()
        sintoma_valor = self.sintoma.get()

        if nombre_virus and sintoma_valor:
            try:
                conexion = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='',
                    db='proyecto_agil'
                )
                cursor = conexion.cursor()

                query = "INSERT INTO Sintomas (nombre, sintoma) VALUES (%s, %s)"
                cursor.execute(query, (nombre_virus, sintoma_valor))
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
        seleccion = self.vistadatos.selection()

        if seleccion:
            sintoma_seleccionado = self.vistadatos.item(seleccion[0], "values")[1]

            try:
                conexion = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='',
                    db='proyecto_agil'
                )
                cursor = conexion.cursor()

                query = "DELETE FROM Sintomas WHERE sintoma = %s"
                cursor.execute(query, (sintoma_seleccionado,))
                conexion.commit()

                messagebox.showinfo("Éxito", "Síntoma eliminado correctamente")

                self.mostrar_datos()

            except pymysql.Error as e:
                messagebox.showerror("Error", f"Error al eliminar síntoma de la base de datos: {e}")

            finally:
                if conexion:
                    conexion.close()
        else:
            messagebox.showwarning("Advertencia", "Seleccione un síntoma para eliminar")

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

            query = "SELECT nombre, sintoma FROM Sintomas"
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
    app = VentanaEliminacionSintomas(root)
    root.mainloop()
