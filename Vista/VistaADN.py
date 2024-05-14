import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from DAO import CRUDVirus
from DAO import CRUDADN
from DTO import cargo_laboral
import pymysql

class VentanaADNS:
    def __init__(self, master):
        self.master = master
        self.master.title("Ingreso de ADN")
        self.master.geometry("600x500")

        self.nombre = tk.StringVar()
        self.sintoma = tk.StringVar()

        self.crear_interfaz()

    def obtener_nombres_virus_desde_bd(self):
        try:
            nombres_virus = [row[1] for row in CRUDVirus.mostrarTodos()]

            return nombres_virus
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener nombres de virus: {e}")

    def crear_interfaz(self):
        self.marco = tk.LabelFrame(self.master, text="Ventana de ingreso de Secuencia de ADN")
        self.marco.place(x=50, y=50, width=500, height=400)

        # Obtener nombres de virus desde la base de datos
        nombres_virus = self.obtener_nombres_virus_desde_bd()

        lblNombre = tk.Label(self.marco, text="Nombre de virus").grid(column=0, row=0, padx=5, pady=5)
        self.lista_virus = ttk.Combobox(self.marco, values=nombres_virus, textvariable=self.nombre)
        self.lista_virus.grid(column=1, row=0)


        lblSintoma = tk.Label(self.marco, text="Secuencia_ADN").grid(column=0, row=1, padx=5, pady=5)
        txtSintoma = tk.Entry(self.marco, textvariable=self.sintoma)
        txtSintoma.grid(column=1, row=1)

        tk.Label(self.marco, text="Aquí van los mensajes", fg="green").grid(column=1, row=2, columnspan=4)

        self.vistadatos = ttk.Treeview(self.marco)
        self.vistadatos.grid(column=1, row=3, columnspan=4)
        self.vistadatos["columns"] = ("nombre", "Secuencia_ADN")
        self.vistadatos.column("#0", width=0, stretch=tk.NO)
        self.vistadatos.column("nombre", width=150, anchor=tk.CENTER)
        self.vistadatos.column("Secuencia_ADN", width=150, anchor=tk.CENTER)
        self.vistadatos.heading("nombre", text="Secuencia de ADN", anchor=tk.CENTER)
        self.vistadatos.heading("Secuencia_ADN", text="Nombre de Virus", anchor=tk.CENTER)

        btnGuardar = tk.Button(self.marco, text="Guardar", command=self.guardar)
        btnGuardar.grid(column=1, row=4)

        self.mostrar_datos()

    def guardar(self):
        nombre_virus = self.nombre.get()
        sintoma = self.sintoma.get()

        if nombre_virus and sintoma:
            try:
                CRUDADN.ingresar(nombre_virus, sintoma)
                messagebox.showinfo("Éxito", "Datos guardados correctamente")

                self.mostrar_datos()

            except Exception as e:
                messagebox.showerror("Error", f"Error al guardar datos en la base de datos: {e}")

        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
    def mostrar_datos(self):
        self.vistadatos.delete(*self.vistadatos.get_children())

        try:
            datos = CRUDADN.mostrarTodos()

            for dato in datos:
                # Utilizar índices [1] y [2] en lugar de [0] y [1]
                self.vistadatos.insert("", "end", values=(dato[1], dato[2]))

        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener datos de la base de datos: {e}")
if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaADNS(root)
    root.mainloop()
