import tkinter as tk
from tkinter import filedialog, messagebox
from os.path import basename
from DAO import CRUDBanco

class VistaBanco:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Vista Banco")
        self.root.geometry("400x200")
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta
        self.label = tk.Label(self.root, text="Seleccione un archivo:")
        self.label.pack(pady=10)

        # Entrada para mostrar el nombre del archivo seleccionado
        self.entry_selected_file = tk.Entry(self.root, state="readonly", width=40)
        self.entry_selected_file.pack(pady=10)

        # Botón estilizado para buscar archivo
        self.button_browse = tk.Button(self.root, text="Buscar Archivo", command=self.browse_file, relief=tk.GROOVE)
        self.button_browse.pack(pady=10)

        # Botón estilizado para subir archivo
        self.button_upload = tk.Button(self.root, text="Subir Archivo", command=self.upload_file, relief=tk.GROOVE)
        self.button_upload.pack(pady=10)

    def browse_file(self):
        self.selected_file = filedialog.askopenfilename(initialdir="/", title="Seleccione un archivo")
        if self.selected_file:
            file_name = basename(self.selected_file)
            self.entry_selected_file.config(state="normal")
            self.entry_selected_file.delete(0, tk.END)
            self.entry_selected_file.insert(0, file_name)
            self.entry_selected_file.config(state="readonly")
        else:
            self.entry_selected_file.delete(0, tk.END)

    def upload_file(self):
        if hasattr(self, 'selected_file') and self.selected_file:
            CRUDBanco.ingresar_direccion_de_archivo(self.selected_file)
            self.show_success_message()

    def show_success_message(self):
        messagebox.showinfo("Éxito", "El archivo se ha agregado correctamente.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    vista = VistaBanco()
    vista.run()
